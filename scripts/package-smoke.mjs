import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import http from "node:http";
import { spawn } from "node:child_process";
import { root, env } from "./environment.mjs";

const temp = fs.mkdtempSync(path.join(os.tmpdir(), "envoapi-consumers-"));
const run = (cmd, args, cwd = root, extra = {}) =>
  new Promise((resolve, reject) => {
    // Consumer processes must import installed packages, never the checkout's Python package.
    const childEnv = { ...env, ...extra };
    delete childEnv.PYTHONPATH;
    const child = spawn(cmd, args, { cwd, env: childEnv });
    let output = "";
    child.stdout.on("data", (d) => (output += d));
    child.stderr.on("data", (d) => (output += d));
    child.on("error", reject);
    child.on("exit", (code) =>
      code === 0
        ? resolve(output)
        : reject(new Error(`${cmd} ${args.join(" ")}\n${output}`)),
    );
  });
let requests = 0;
const posts = fs.readFileSync(path.join(root, "tests/fixtures/posts.json"));
const server = http.createServer((req, res) => {
  if (
    req.headers.authorization !== "Bearer package-test" ||
    req.url !== "/v1/profiles/posts?username=alice"
  ) {
    res.writeHead(400);
    res.end("unexpected SDK request");
    return;
  }
  requests++;
  res.writeHead(200, {
    "content-type": "application/json",
    "x-request-id": "req_packages",
  });
  res.end(posts);
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const extra = {
  ENVOAPI_API_KEY: "package-test",
  ENVOAPI_BASE_URL: `http://127.0.0.1:${server.address().port}`,
};
try {
  fs.mkdirSync(path.join(root, "dist"), { recursive: true });
  await run("pnpm", ["--filter", "envoapi", "build"]);
  await run("pnpm", [
    "--dir",
    "typescript",
    "pack",
    "--pack-destination",
    "../dist",
  ]);
  const js = path.join(temp, "javascript");
  fs.mkdirSync(js);
  fs.writeFileSync(
    path.join(js, "package.json"),
    JSON.stringify({ name: "sdk-consumer", private: true, type: "module" }),
  );
  await run("pnpm", ["add", path.join(root, "dist/envoapi-0.1.0.tgz")], js);
  fs.copyFileSync(
    path.join(root, "examples/typescript/posts.mjs"),
    path.join(js, "posts.mjs"),
  );
  const jsOutput = await run(process.execPath, ["posts.mjs"], js, extra);
  if (JSON.parse(jsOutput).creditCost !== 1)
    throw new Error("TypeScript package lost metadata");
  fs.writeFileSync(
    path.join(js, "check.ts"),
    `import {EnvoAPI} from 'envoapi';\nconst client=new EnvoAPI({apiKey:'test'});\nconst response=await client.profiles.getPosts({username:'alice'});\nconst credits: number=response.body.meta.creditCost;\n// @ts-expect-error username is required\nclient.profiles.getPosts({});\n// @ts-expect-error credits are numeric\nconst invalid: string=response.body.meta.creditCost;\n`,
  );
  await run(
    path.join(root, "node_modules/.bin/tsc"),
    [
      "--noEmit",
      "--strict",
      "--target",
      "ES2022",
      "--module",
      "NodeNext",
      "--moduleResolution",
      "NodeNext",
      "check.ts",
    ],
    js,
  );

  await run("python", [
    "-m",
    "build",
    "--wheel",
    "--no-isolation",
    "python",
    "--outdir",
    "dist",
  ]);
  const py = path.join(temp, "python");
  fs.mkdirSync(py);
  await run("uv", [
    "venv",
    path.join(py, ".venv"),
    "--python",
    path.join(root, ".venv/bin/python"),
  ]);
  const interpreter = path.join(py, ".venv/bin/python");
  await run("uv", [
    "pip",
    "install",
    "--python",
    interpreter,
    path.join(root, "dist/envoapi-0.1.0-py3-none-any.whl"),
  ]);
  for (const name of ["posts.py", "async_posts.py"]) {
    fs.copyFileSync(
      path.join(root, "examples/python", name),
      path.join(py, name),
    );
    const output = await run(interpreter, [name], py, extra);
    if (!output.includes("'creditCost': 1"))
      throw new Error("Python package lost metadata");
  }
  await run(
    interpreter,
    [
      "-c",
      `import envoapi; from pathlib import Path; assert '${root}' not in envoapi.__file__; assert Path(envoapi.__file__).with_name('py.typed').exists()`,
    ],
    py,
  );

  const go = path.join(temp, "go");
  fs.mkdirSync(go);
  // Copy the module to prove the consumer needs neither the monorepo root nor backend checkout.
  const module = path.join(temp, "go-sdk");
  fs.cpSync(path.join(root, "go"), module, { recursive: true });
  fs.writeFileSync(
    path.join(go, "go.mod"),
    `module sdk-consumer\n\ngo 1.25.0\nrequire github.com/envoapi-official/envoapi-sdks/go v0.0.0\nreplace github.com/envoapi-official/envoapi-sdks/go => ${module}\n`,
  );
  fs.copyFileSync(
    path.join(root, "examples/go/main.go"),
    path.join(go, "main.go"),
  );
  await run("go", ["mod", "tidy"], go);
  const goOutput = await run("go", ["run", "."], go, extra);
  if (JSON.parse(goOutput).meta.creditCost !== 1)
    throw new Error("Go package lost metadata");
  if (requests !== 4)
    throw new Error(`Expected four example requests, got ${requests}`);
  console.log(
    "npm archive, Python wheel (sync and async), and isolated Go module passed consumer checks.",
  );
} finally {
  await new Promise((resolve) => server.close(resolve));
  fs.rmSync(temp, { recursive: true, force: true });
}
