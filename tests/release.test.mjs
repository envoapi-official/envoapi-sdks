import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { execFileSync } from "node:child_process";
import {
  planReleases,
  pendingFiles,
  registryJSON,
  pushRelease,
  prepareRelease,
  sealRelease,
  readVersions,
  validateBundle,
  checkPublication,
  releaseIsPushed,
  withSnapshot,
} from "../scripts/release.mjs";

const versions = { npm: "0.1.3", python: "0.1.2", go: "0.1.3" };
const previous = {
  npm: { version: "0.1.3", tag: "npm/v0.1.3" },
  python: { version: "0.1.2", tag: "python/v0.1.2" },
  go: { version: "0.1.3", tag: "go/v0.1.3" },
};
const changes = (files) => ({ npm: files, python: files, go: files });
const select = (files, overrides = {}) =>
  planReleases({ versions, previous, changes: changes(files), ...overrides });

test("a language change increments only that SDK's patch version", () => {
  assert.deepEqual(select(["python/envoapi/runtime.py"]), [
    {
      kind: "python",
      version: "0.1.3",
      tag: "python/v0.1.3",
      previous: "python/v0.1.2",
    },
  ]);
});

test("explicit higher versions take precedence over patch increments", () => {
  assert.equal(
    select(["typescript/package.json"], {
      versions: { ...versions, npm: "0.2.0" },
    })[0].version,
    "0.2.0",
  );
  assert.equal(
    select(["go/client.go"], {
      versions: { ...versions, go: "1.0.0" },
    })[0].version,
    "1.0.0",
  );
});

test("shared contract and build inputs release all three SDKs", () => {
  for (const file of [
    "openapi/public-v1.yaml",
    "scripts/generate.mjs",
    "package.json",
    "pnpm-lock.yaml",
    "requirements-dev.lock",
    "LICENSE",
  ]) {
    assert.deepEqual(
      select([file]).map(({ tag }) => tag),
      ["npm/v0.1.4", "python/v0.1.3", "go/v0.1.4"],
      file,
    );
  }
});

test("root documentation, examples, and CI changes do not publish packages", () => {
  assert.deepEqual(
    select([
      "README.md",
      "CHANGELOG.md",
      "docs/operations.md",
      "examples/go/main.go",
      ".github/workflows/ci.yml",
      "tests/release.test.mjs",
    ]),
    [],
  );
});

test("change detection uses the independent baseline for each SDK", () => {
  assert.deepEqual(
    select([], {
      changes: { npm: ["typescript/README.md"], python: [], go: [] },
    }).map(({ kind }) => kind),
    ["npm"],
  );
});

test("missing npm and Python tags bootstrap from published versions", () => {
  assert.deepEqual(
    select([], {
      previous: {
        ...previous,
        npm: { version: "0.1.3", tag: null },
        python: { version: "0.1.2", tag: null },
      },
    }).map(({ tag }) => tag),
    ["npm/v0.1.4", "python/v0.1.3"],
  );
});

test("downgrades, prereleases, and unsupported Go module majors are rejected", () => {
  for (const [kind, version] of [
    ["npm", "0.1.2"],
    ["python", "0.2.0-rc.1"],
    ["go", "2.0.0"],
  ]) {
    assert.throws(
      () =>
        select(["scripts/generate.mjs"], {
          versions: { ...versions, [kind]: version },
        }),
      /downgrade|stable|module/i,
    );
  }
});

test("npm retries skip identical archives and reject conflicting archives", () => {
  const files = [{ name: "envoapi-0.1.4.tgz", integrity: "sha512-matching" }];
  assert.deepEqual(pendingFiles("npm", files, null), files);
  assert.deepEqual(
    pendingFiles("npm", files, { dist: { integrity: "sha512-matching" } }),
    [],
  );
  assert.throws(
    () =>
      pendingFiles("npm", files, { dist: { integrity: "sha512-different" } }),
    /conflict/i,
  );
});

test("Python retries upload only missing files and reject changed file contents", () => {
  const files = [
    { name: "envoapi-0.1.3-py3-none-any.whl", sha256: "wheel-hash" },
    { name: "envoapi-0.1.3.tar.gz", sha256: "sdist-hash" },
  ];
  const registry = {
    urls: [{ filename: files[0].name, digests: { sha256: "wheel-hash" } }],
  };
  assert.deepEqual(pendingFiles("python", files, registry), [files[1]]);
  registry.urls[0].digests.sha256 = "different";
  assert.throws(() => pendingFiles("python", files, registry), /conflict/i);
});

test("registry errors cannot be mistaken for an unpublished version", async () => {
  assert.equal(
    await registryJSON(
      "https://registry.invalid",
      async () => new Response("", { status: 404 }),
    ),
    null,
  );
  for (const status of [401, 403, 429, 500]) {
    await assert.rejects(
      registryJSON(
        "https://registry.invalid",
        async () => new Response("", { status }),
      ),
      new RegExp(String(status)),
    );
  }
});

const git = (cwd, ...args) =>
  execFileSync("git", args, {
    cwd,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
  }).trim();

function repository(t) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "envoapi-release-test-"));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  const remote = path.join(dir, "remote.git");
  const work = path.join(dir, "work");
  git(dir, "init", "--bare", "--initial-branch=main", remote);
  git(dir, "clone", remote, work);
  git(work, "config", "user.name", "Release test");
  git(work, "config", "user.email", "test@example.invalid");
  fs.writeFileSync(path.join(work, "source"), "initial");
  git(work, "add", ".");
  git(work, "commit", "-m", "initial");
  const source = git(work, "rev-parse", "HEAD");
  git(work, "push", "origin", "main");
  fs.writeFileSync(path.join(work, "source"), "version bump");
  git(work, "commit", "-am", "release");
  const commit = git(work, "rev-parse", "HEAD");
  return {
    work,
    remote,
    source,
    commit,
    releases: [{ kind: "go", tag: "go/v0.1.4", version: "0.1.4", files: [] }],
  };
}

test("a verified release pushes the version commit and Go tag together", (t) => {
  const state = repository(t);
  assert.equal(pushRelease(state.work, state), true);
  assert.equal(git(state.remote, "rev-parse", "refs/heads/main"), state.commit);
  assert.equal(git(state.remote, "rev-parse", "go/v0.1.4^{}"), state.commit);
});

test("a newer main commit prevents stale publication", (t) => {
  const state = repository(t);
  git(state.work, "push", "origin", `${state.commit}:main`);
  assert.equal(pushRelease(state.work, state), false);
  assert.equal(git(state.remote, "tag", "--list"), "");
});

test("a conflicting tag rejects the entire push without advancing main", (t) => {
  const state = repository(t);
  git(state.remote, "tag", "go/v0.1.4", state.source);
  assert.throws(() => pushRelease(state.work, state));
  assert.equal(git(state.remote, "rev-parse", "refs/heads/main"), state.source);
  assert.equal(git(state.remote, "rev-parse", "go/v0.1.4"), state.source);
});

function sdkRepository(t) {
  const state = repository(t);
  const files = {
    "typescript/package.json": JSON.stringify({
      name: "envoapi",
      version: "0.1.3",
    }),
    "typescript/src/runtime.ts":
      'const headers = { "User-Agent": "envoapi-typescript/0.1.3" };\n',
    "python/pyproject.toml": '[project]\nname = "envoapi"\nversion = "0.1.2"\n',
    "python/envoapi/runtime.py":
      'headers = {"User-Agent": "envoapi-python/0.1.2"}\n',
    "go/client.go": 'package envoapi\nconst sdkVersion = "0.1.3"\n',
    ".gitignore": "dist/\n",
  };
  for (const [name, content] of Object.entries(files)) {
    fs.mkdirSync(path.dirname(path.join(state.work, name)), {
      recursive: true,
    });
    fs.writeFileSync(path.join(state.work, name), content);
  }
  git(state.work, "add", ".");
  git(state.work, "commit", "-m", "SDK source");
  state.source = git(state.work, "rev-parse", "HEAD");
  git(state.work, "push", "origin", "main");
  return state;
}

const publishedVersions = async (url) => {
  if (url === "https://registry.npmjs.org/envoapi/latest")
    return Response.json({ version: "0.1.3" });
  if (url === "https://pypi.org/pypi/envoapi/json")
    return Response.json({ info: { version: "0.1.2" } });
  return new Response("", { status: 404 });
};

function packages(cwd) {
  for (const [kind, names] of Object.entries({
    npm: ["envoapi-0.1.4.tgz"],
    python: ["envoapi-0.1.3-py3-none-any.whl", "envoapi-0.1.3.tar.gz"],
  })) {
    fs.mkdirSync(path.join(cwd, "dist/packages", kind), { recursive: true });
    for (const name of names)
      fs.writeFileSync(path.join(cwd, "dist/packages", kind, name), name);
  }
}

test("release preparation bumps versions without moving Git refs", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  assert.deepEqual(readVersions(state.work), {
    npm: "0.1.4",
    python: "0.1.3",
    go: "0.1.4",
  });
  assert.equal(git(state.work, "rev-parse", "HEAD"), state.source);
  assert.equal(git(state.remote, "rev-parse", "main"), state.source);
  assert.equal(plan.source, state.source);
  assert.equal(plan.releases.length, 3);
});

test("release preparation refuses a dirty checkout", async (t) => {
  const state = sdkRepository(t);
  fs.appendFileSync(path.join(state.work, "source"), "uncommitted edit");
  await assert.rejects(
    prepareRelease(state.work, { fetcher: publishedVersions }),
    /clean/i,
  );
});

test("the bundle preserves exact archives and tags the matching version commit", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  const bundle = path.join(state.work, "dist/release");
  validateBundle(bundle, plan);
  assert.equal(
    fs.readFileSync(path.join(bundle, "python/envoapi-0.1.3.tar.gz"), "utf8"),
    "envoapi-0.1.3.tar.gz",
  );
  assert.equal(pushRelease(state.work, plan), true);
  assert.equal(
    JSON.parse(git(state.remote, "show", "npm/v0.1.4:typescript/package.json"))
      .version,
    "0.1.4",
  );
  assert.equal(git(state.remote, "rev-parse", "go/v0.1.4^{}"), plan.commit);
  fs.appendFileSync(path.join(bundle, "npm/envoapi-0.1.4.tgz"), "changed");
  assert.throws(() => validateBundle(bundle, plan), /hash|checksum/i);
});

test("sealing cannot accidentally commit changes outside version files", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  fs.appendFileSync(
    path.join(state.work, "source"),
    "unexpected generation drift",
  );
  assert.throws(() => sealRelease(state.work, plan), /unexpected/i);
  assert.equal(git(state.work, "rev-parse", "HEAD"), state.source);
});

test("an incomplete previous publication blocks new version bumps", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  pushRelease(state.work, plan);
  await assert.rejects(
    prepareRelease(state.work, { fetcher: publishedVersions }),
    /incomplete|rerun/i,
  );
  assert.deepEqual(readVersions(state.work), {
    npm: "0.1.4",
    python: "0.1.3",
    go: "0.1.4",
  });
});

test("publication checks stage only missing artifacts from the saved bundle", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  const wheel = plan.releases.find(({ kind }) => kind === "python").files[0];
  const fetcher = async () =>
    Response.json({
      urls: [{ filename: wheel.name, digests: { sha256: wheel.sha256 } }],
    });
  const output = await checkPublication(
    path.join(state.work, "dist/release"),
    "python",
    fetcher,
  );
  assert.deepEqual(output, ["envoapi-0.1.3.tar.gz"]);
  assert.deepEqual(
    fs.readdirSync(path.join(state.work, "dist/release/upload-python")),
    ["envoapi-0.1.3.tar.gz"],
  );
});

test("a retry recognizes its published tags even after main advances", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  assert.equal(releaseIsPushed(state.work, plan), false);
  pushRelease(state.work, plan);
  fs.appendFileSync(path.join(state.work, "source"), "next update");
  git(state.work, "commit", "-am", "next update");
  git(state.work, "push", "origin", "main");
  assert.equal(releaseIsPushed(state.work, plan), true);
});

test("retry refuses a partial set of tags or a tag at another commit", (t) => {
  const state = repository(t);
  git(
    state.remote,
    "-c",
    "user.name=Test",
    "-c",
    "user.email=test@example.invalid",
    "tag",
    "-a",
    "go/v0.1.4",
    state.source,
    "-m",
    "conflicting tag",
  );
  assert.throws(() => releaseIsPushed(state.work, state), /conflict/i);
  state.releases.push({
    kind: "npm",
    version: "0.1.4",
    tag: "npm/v0.1.4",
    files: [],
  });
  assert.throws(() => releaseIsPushed(state.work, state), /conflict/i);
});

test("an explicit version already stamped in source still gets a release commit", async (t) => {
  const state = sdkRepository(t);
  git(state.work, "tag", "go/v0.1.3", state.commit);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  git(state.work, "commit", "-am", "explicit next versions");
  const source = git(state.work, "rev-parse", "HEAD");
  const explicit = await prepareRelease(state.work, {
    fetcher: publishedVersions,
  });
  assert.deepEqual(explicit.releases, plan.releases);
  packages(state.work);
  sealRelease(state.work, explicit);
  assert.notEqual(explicit.commit, source);
  assert.equal(git(state.work, "rev-parse", "HEAD^"), source);
});

test("dry runs include local edits but keep the original checkout, index, refs, and artifacts intact", async (t) => {
  const state = sdkRepository(t);
  fs.writeFileSync(path.join(state.work, "untracked"), "new source");
  fs.appendFileSync(path.join(state.work, "source"), "local edit");
  git(state.work, "add", "source");
  fs.mkdirSync(path.join(state.work, "dist"));
  fs.writeFileSync(path.join(state.work, "dist/keep"), "existing artifact");
  const before = git(state.work, "status", "--porcelain");
  let snapshot;
  await withSnapshot(state.work, async (cwd) => {
    snapshot = cwd;
    assert.equal(
      fs.readFileSync(path.join(cwd, "untracked"), "utf8"),
      "new source",
    );
    assert.match(
      fs.readFileSync(path.join(cwd, "source"), "utf8"),
      /local edit$/,
    );
    const plan = await prepareRelease(cwd, { fetcher: publishedVersions });
    packages(cwd);
    sealRelease(cwd, plan);
    validateBundle(path.join(cwd, "dist/release"), plan);
  });
  assert.equal(fs.existsSync(snapshot), false);
  assert.equal(git(state.work, "status", "--porcelain"), before);
  assert.equal(git(state.work, "rev-parse", "HEAD"), state.source);
  assert.equal(git(state.remote, "rev-parse", "main"), state.source);
  assert.equal(git(state.remote, "tag", "--list"), "");
  assert.equal(
    fs.readFileSync(path.join(state.work, "dist/keep"), "utf8"),
    "existing artifact",
  );
  assert.deepEqual(readVersions(state.work), versions);
});

test("completed releases ignore root docs and use each SDK tag for the next change", async (t) => {
  const state = sdkRepository(t);
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  pushRelease(state.work, plan);
  const npm = plan.releases.find(({ kind }) => kind === "npm");
  const python = plan.releases.find(({ kind }) => kind === "python");
  const fetcher = async (url) =>
    Response.json(
      url.includes("registry.npmjs.org")
        ? { version: npm.version, dist: { integrity: npm.files[0].integrity } }
        : {
            urls: python.files.map((file) => ({
              filename: file.name,
              digests: { sha256: file.sha256 },
            })),
          },
    );
  fs.writeFileSync(
    path.join(state.work, "README.md"),
    "Root documentation update",
  );
  git(state.work, "add", "README.md");
  git(state.work, "commit", "-m", "docs");
  assert.deepEqual(
    (await prepareRelease(state.work, { fetcher })).releases,
    [],
  );
  fs.writeFileSync(
    path.join(state.work, "python/README.md"),
    "Python package documentation update",
  );
  git(state.work, "add", "python/README.md");
  git(state.work, "commit", "-m", "Python docs");
  assert.deepEqual((await prepareRelease(state.work, { fetcher })).releases, [
    {
      kind: "python",
      version: "0.1.4",
      tag: "python/v0.1.4",
      previous: "python/v0.1.3",
    },
  ]);
});

test("the workflow CLI resumes from its original source and saved bundle without stamping again", async (t) => {
  const state = sdkRepository(t);
  fs.mkdirSync(path.join(state.work, "scripts"));
  fs.copyFileSync(
    new URL("../scripts/release.mjs", import.meta.url),
    path.join(state.work, "scripts/release.mjs"),
  );
  git(state.work, "add", "scripts");
  git(state.work, "commit", "-m", "release workflow helper");
  git(state.work, "push", "origin", "main");
  const plan = await prepareRelease(state.work, { fetcher: publishedVersions });
  packages(state.work);
  sealRelease(state.work, plan);
  pushRelease(state.work, plan);
  git(state.work, "checkout", "--detach", plan.source);
  const result = execFileSync(
    process.execPath,
    ["scripts/release.mjs", "prepare"],
    {
      cwd: state.work,
      encoding: "utf8",
      env: {
        ...process.env,
        GITHUB_SHA: plan.source,
        RESTORED_ARTIFACT: "sdk-release-123-1",
        GITHUB_OUTPUT: path.join(state.work, "dist/job-output"),
      },
    },
  );
  assert.match(result, /resumed=true/);
  assert.match(result, /artifact=sdk-release-123-1/);
  assert.match(result, /npm=true\npython=true\ngo=true/);
  assert.deepEqual(readVersions(state.work), versions);
  assert.equal(git(state.work, "rev-parse", "HEAD"), plan.source);
  assert.equal(git(state.remote, "rev-parse", "main"), plan.commit);
  validateBundle(path.join(state.work, "dist/release"), plan);
});
