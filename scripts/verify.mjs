import { spawnSync } from "node:child_process";
import { root, env } from "./environment.mjs";
const run = (cmd, args) => {
  console.log(`\n> ${cmd} ${args.join(" ")}`);
  const r = spawnSync(cmd, args, {
    cwd: root,
    env: args.includes("-race") ? { ...env, CGO_ENABLED: "1" } : env,
    stdio: "inherit",
  });
  if (r.status !== 0) process.exit(r.status ?? 1);
};
run("pnpm", ["--filter", "envoapi", "build"]);
run("node", ["--test", "typescript/test/client.test.mjs"]);
run("python", ["-m", "pytest", "-q", "python/tests"]);
run("python", ["-m", "mypy", "python/envoapi", "--follow-imports=silent"]);
run("go", ["-C", "go", "test", "-race", "./..."]);
run("go", ["-C", "go", "vet", "./..."]);
run("node", [
  "--test",
  "tests/generation.test.mjs",
  "tests/import.test.mjs",
  "tests/packages.test.mjs",
]);
console.log("\nAll local SDK verification passed.");
