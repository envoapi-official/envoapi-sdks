import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { fileURLToPath, pathToFileURL } from "node:url";

const kinds = ["npm", "python", "go"];
const directories = { npm: "typescript", python: "python", go: "go" };
const bot = [
  "-c",
  "user.name=github-actions[bot]",
  "-c",
  "user.email=41898282+github-actions[bot]@users.noreply.github.com",
];
const git = (cwd, ...args) =>
  execFileSync("git", args, {
    cwd,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
  }).trim();

function parts(version) {
  if (!/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/.test(version)) {
    throw new Error(`Expected a stable X.Y.Z version, got ${version}`);
  }
  const result = version.split(".").map(Number);
  if (!result.every(Number.isSafeInteger))
    throw new Error("Version is too large");
  return result;
}

function compare(a, b) {
  const left = parts(a),
    right = parts(b);
  for (let i = 0; i < 3; i++)
    if (left[i] !== right[i]) return left[i] - right[i];
  return 0;
}

export function planReleases({ versions, previous, changes }) {
  const releases = [];
  for (const kind of kinds) {
    const current = versions[kind];
    const base = previous[kind];
    const difference = compare(current, base.version);
    if (difference < 0)
      throw new Error(
        `${kind}: version downgrade from ${base.version} to ${current}`,
      );
    if (kind === "go" && parts(current)[0] >= 2)
      throw new Error("Go v2+ requires a module path migration");
    const affected = changes[kind].some(
      (file) =>
        file.startsWith(`${directories[kind]}/`) ||
        file.startsWith("openapi/") ||
        file.startsWith("scripts/") ||
        [
          "package.json",
          "pnpm-lock.yaml",
          "pnpm-workspace.yaml",
          "requirements-dev.lock",
          "LICENSE",
        ].includes(file),
    );
    if (!base.tag || affected || difference > 0) {
      const next = parts(base.version);
      next[2]++;
      const version = difference > 0 ? current : next.join(".");
      parts(version);
      releases.push({
        kind,
        version,
        tag: `${kind}/v${version}`,
        previous: base.tag,
      });
    }
  }
  return releases;
}

export function pendingFiles(kind, files, registry) {
  if (!registry) return files;
  return files.filter((file) => {
    const published =
      kind === "npm"
        ? registry.dist
        : registry.urls?.find((item) => item.filename === file.name);
    if (!published && kind !== "npm") return true;
    const matches =
      kind === "npm"
        ? published?.integrity?.split(/\s+/).includes(file.integrity)
        : published.digests?.sha256 === file.sha256;
    if (!matches) throw new Error(`Published artifact conflict: ${file.name}`);
    return false;
  });
}

export async function registryJSON(url, fetcher = fetch) {
  const response = await fetcher(url, { signal: AbortSignal.timeout(30_000) });
  if (response.status === 404) return null;
  if (!response.ok)
    throw new Error(`Registry request failed (${response.status}): ${url}`);
  return response.json();
}

export function pushRelease(cwd, plan) {
  const tip = git(cwd, "ls-remote", "origin", "refs/heads/main").split(/\s/)[0];
  if (tip !== plan.source) return false;
  for (const release of plan.releases) {
    const message = `EnvoAPI ${release.tag}\n\n${JSON.stringify({ source: plan.source, run: plan.run, files: release.files })}`;
    git(cwd, ...bot, "tag", "-a", release.tag, plan.commit, "-m", message);
  }
  git(
    cwd,
    "push",
    "--atomic",
    "origin",
    `${plan.commit}:refs/heads/main`,
    ...plan.releases.map(({ tag }) => `refs/tags/${tag}`),
  );
  return true;
}

const read = (cwd, name) => fs.readFileSync(path.join(cwd, name), "utf8");
const metadataFiles = {
  npm: ["typescript/package.json", "typescript/src/runtime.ts"],
  python: ["python/pyproject.toml", "python/envoapi/runtime.py"],
  go: ["go/client.go"],
};
const packageNames = (kind, version) =>
  kind === "npm"
    ? [`envoapi-${version}.tgz`]
    : kind === "python"
      ? [`envoapi-${version}-py3-none-any.whl`, `envoapi-${version}.tar.gz`]
      : [];
const registryURL = (kind, version) =>
  kind === "npm"
    ? `https://registry.npmjs.org/envoapi/${version ?? "latest"}`
    : `https://pypi.org/pypi/envoapi/${version ? `${version}/` : ""}json`;

export function readVersions(cwd) {
  return {
    npm: JSON.parse(read(cwd, metadataFiles.npm[0])).version,
    python: read(cwd, metadataFiles.python[0]).match(
      /^version = "([^"]+)"$/m,
    )?.[1],
    go: read(cwd, metadataFiles.go[0]).match(
      /^const sdkVersion = "([^"]+)"$/m,
    )?.[1],
  };
}

function replaceOnce(cwd, name, pattern, replacement) {
  const text = read(cwd, name);
  if (
    [
      ...text.matchAll(
        new RegExp(pattern.source, `${pattern.flags.replace("g", "")}g`),
      ),
    ].length !== 1
  ) {
    throw new Error(`Expected exactly one version field in ${name}`);
  }
  fs.writeFileSync(path.join(cwd, name), text.replace(pattern, replacement));
}

export async function prepareRelease(cwd, { fetcher = fetch, run = "" } = {}) {
  if (git(cwd, "status", "--porcelain"))
    throw new Error("Release preparation requires a clean checkout");
  const source = git(cwd, "rev-parse", "HEAD");
  const versions = readVersions(cwd);
  const previous = {},
    changes = {};
  for (const kind of kinds) {
    const tags = git(cwd, "tag", "--list", `${kind}/v*`)
      .split("\n")
      .filter((tag) => new RegExp(`^${kind}/v\\d+\\.\\d+\\.\\d+$`).test(tag))
      .sort((a, b) => compare(a.split("/v")[1], b.split("/v")[1]));
    const tag = tags.at(-1) ?? null;
    let version = tag?.split("/v")[1];
    if (kind !== "go") {
      const registry = await registryJSON(registryURL(kind, version), fetcher);
      if (tag) {
        const message = git(
          cwd,
          "for-each-ref",
          "--format=%(contents)",
          `refs/tags/${tag}`,
        );
        const info = message.includes("\n\n{")
          ? JSON.parse(message.slice(message.indexOf("\n\n{") + 2))
          : null;
        if (!info?.files?.length)
          throw new Error(
            `Missing artifact hashes on ${tag}; reconcile this tag before enabling releases`,
          );
        if (pendingFiles(kind, info.files, registry).length) {
          throw new Error(
            `Incomplete publication for ${tag}. Rerun the failed jobs: ${info.run || "the original release workflow"}`,
          );
        }
      } else {
        version =
          (kind === "npm" ? registry?.version : registry?.info?.version) ??
          "0.0.0";
      }
    }
    // Go has no package registry; before its first tag the source version is the baseline.
    previous[kind] = { tag, version: version ?? versions[kind] };
    changes[kind] = tag
      ? git(cwd, "diff", "--name-only", tag, source).split("\n")
      : [];
  }
  const releases = planReleases({ versions, previous, changes });
  for (const { kind, version } of releases) {
    if (kind === "npm") {
      const name = metadataFiles.npm[0];
      const pkg = JSON.parse(read(cwd, name));
      pkg.version = version;
      fs.writeFileSync(
        path.join(cwd, name),
        `${JSON.stringify(pkg, null, 2)}\n`,
      );
    } else if (kind === "python") {
      replaceOnce(
        cwd,
        metadataFiles.python[0],
        /^version = "[^"]+"$/m,
        `version = "${version}"`,
      );
    } else {
      replaceOnce(
        cwd,
        metadataFiles.go[0],
        /^const sdkVersion = "[^"]+"$/m,
        `const sdkVersion = "${version}"`,
      );
    }
    if (kind !== "go") {
      replaceOnce(
        cwd,
        metadataFiles[kind][1],
        new RegExp(`envoapi-${directories[kind]}/[0-9.]+`),
        `envoapi-${directories[kind]}/${version}`,
      );
    }
  }
  return { source, run, releases };
}

function digest(file) {
  const bytes = fs.readFileSync(file);
  return {
    sha256: createHash("sha256").update(bytes).digest("hex"),
    integrity: `sha512-${createHash("sha512").update(bytes).digest("base64")}`,
  };
}

export function sealRelease(cwd, plan) {
  if (!plan.releases.length) return;
  if (git(cwd, "rev-parse", "HEAD") !== plan.source)
    throw new Error("Release source commit changed");
  const allowed = plan.releases.flatMap(({ kind }) => metadataFiles[kind]);
  const changed = git(cwd, "diff", "HEAD", "--name-only")
    .split("\n")
    .filter(Boolean);
  const untracked = git(cwd, "ls-files", "--others", "--exclude-standard")
    .split("\n")
    .filter(Boolean);
  if ([...changed, ...untracked].some((name) => !allowed.includes(name)))
    throw new Error("Unexpected changes outside release version files");
  fs.rmSync(path.join(cwd, "dist/release"), { recursive: true, force: true });
  for (const release of plan.releases) {
    const output = path.join(cwd, "dist/release", release.kind);
    fs.mkdirSync(output, { recursive: true });
    release.files = packageNames(release.kind, release.version).map((name) => {
      const file = path.join(cwd, "dist/packages", release.kind, name);
      const hashes = digest(file);
      fs.copyFileSync(file, path.join(output, name));
      return { name, ...hashes };
    });
  }
  git(cwd, "add", "--", ...allowed);
  git(
    cwd,
    ...bot,
    "commit",
    "--no-gpg-sign",
    "--allow-empty",
    "-m",
    `chore: release ${plan.releases.map(({ kind, version }) => `${kind} ${version}`).join(", ")}\n\nRelease-Source: ${plan.source}\n${plan.run}`,
  );
  plan.commit = git(cwd, "rev-parse", "HEAD");
  fs.writeFileSync(
    path.join(cwd, "dist/release/plan.json"),
    `${JSON.stringify(plan, null, 2)}\n`,
  );
}

export function validateBundle(dir, plan) {
  for (const release of plan.releases) {
    if (
      !kinds.includes(release.kind) ||
      release.tag !== `${release.kind}/v${release.version}`
    )
      throw new Error("Invalid release bundle");
    parts(release.version);
    const names = packageNames(release.kind, release.version);
    if (
      JSON.stringify(release.files.map(({ name }) => name)) !==
      JSON.stringify(names)
    )
      throw new Error("Unexpected release artifacts");
    for (const file of release.files) {
      const actual = digest(path.join(dir, release.kind, file.name));
      if (actual.sha256 !== file.sha256 || actual.integrity !== file.integrity)
        throw new Error(`Artifact checksum mismatch: ${file.name}`);
    }
  }
}

export async function checkPublication(dir, kind, fetcher = fetch) {
  const plan = JSON.parse(read(dir, "plan.json"));
  validateBundle(dir, plan);
  const release = plan.releases.find((item) => item.kind === kind);
  if (!release) throw new Error(`No ${kind} release in bundle`);
  const registry = await registryJSON(
    registryURL(kind, release.version),
    fetcher,
  );
  const pending = pendingFiles(kind, release.files, registry);
  if (kind === "npm" && pending.length) {
    const latest = await registryJSON(registryURL(kind), fetcher);
    if (latest && compare(latest.version, release.version) > 0)
      throw new Error(
        "Refusing to move npm latest backwards; reconcile the newer publication",
      );
  }
  const output = path.join(dir, `upload-${kind}`);
  fs.rmSync(output, { recursive: true, force: true });
  fs.mkdirSync(output, { recursive: true });
  for (const file of pending)
    fs.copyFileSync(
      path.join(dir, kind, file.name),
      path.join(output, file.name),
    );
  return pending.map(({ name }) => name);
}

export function releaseIsPushed(cwd, plan) {
  const refs = Object.fromEntries(
    git(
      cwd,
      "ls-remote",
      "origin",
      ...plan.releases.flatMap(({ tag }) => [
        `refs/tags/${tag}`,
        `refs/tags/${tag}^{}`,
      ]),
    )
      .split("\n")
      .filter(Boolean)
      .map((line) => line.split(/\s+/).reverse()),
  );
  if (!Object.keys(refs).length) return false;
  if (
    plan.releases.some(({ tag }) => refs[`refs/tags/${tag}^{}`] !== plan.commit)
  ) {
    throw new Error(
      "Release tag conflict: the saved bundle does not match the remote tags",
    );
  }
  return true;
}

export async function withSnapshot(cwd, action) {
  const temp = fs.mkdtempSync(
    path.join(os.tmpdir(), "envoapi-release-dry-run-"),
  );
  const snapshot = path.join(temp, "checkout");
  try {
    git(temp, "clone", "--no-hardlinks", cwd, snapshot);
    const files = git(
      cwd,
      "ls-files",
      "--cached",
      "--others",
      "--exclude-standard",
      "-z",
    )
      .split("\0")
      .filter(Boolean);
    for (const name of new Set(files)) {
      const source = path.join(cwd, name),
        target = path.join(snapshot, name);
      fs.rmSync(target, { recursive: true, force: true });
      if (fs.existsSync(source)) {
        fs.mkdirSync(path.dirname(target), { recursive: true });
        fs.cpSync(source, target, { recursive: true });
      }
    }
    // Reuse installed tools; all generated files and release commits stay in the snapshot.
    for (const name of [
      "node_modules",
      "typescript/node_modules",
      ".venv",
      ".tools",
    ]) {
      if (fs.existsSync(path.join(cwd, name)))
        fs.symlinkSync(path.join(cwd, name), path.join(snapshot, name), "dir");
    }
    git(snapshot, "add", "-A");
    git(
      snapshot,
      ...bot,
      "commit",
      "--no-gpg-sign",
      "--allow-empty",
      "-m",
      "Local release dry run",
    );
    return await action(snapshot);
  } finally {
    fs.rmSync(temp, { recursive: true, force: true });
  }
}

async function github(endpoint, body) {
  const response = await fetch(
    `https://api.github.com/repos/${process.env.GITHUB_REPOSITORY}/${endpoint}`,
    {
      method: body ? "POST" : "GET",
      headers: {
        Authorization: `Bearer ${process.env.GH_TOKEN}`,
        Accept: "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        ...(body ? { "Content-Type": "application/json" } : {}),
      },
      ...(body ? { body: JSON.stringify(body) } : {}),
      signal: AbortSignal.timeout(30_000),
    },
  );
  if (!body && response.status === 404) return null;
  if (!response.ok)
    throw new Error(`GitHub request failed (${response.status}): ${endpoint}`);
  return response.json();
}

function output(name, value) {
  if (process.env.GITHUB_OUTPUT)
    fs.appendFileSync(process.env.GITHUB_OUTPUT, `${name}=${value}\n`);
  console.log(`${name}=${value}`);
}

async function main() {
  const cwd = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
  const dir = path.join(cwd, "dist/release");
  const command = process.argv[2];
  if (command === "dry-run") {
    await withSnapshot(cwd, async (snapshot) => {
      const plan = await prepareRelease(snapshot);
      execFileSync("pnpm", ["verify"], { cwd: snapshot, stdio: "inherit" });
      sealRelease(snapshot, plan);
      if (plan.releases.length)
        validateBundle(path.join(snapshot, "dist/release"), plan);
      console.log("\nDry run passed. No pushes or uploads were made.");
      console.log(JSON.stringify(plan.releases, null, 2));
    });
    return;
  }
  if (command === "find-artifact") {
    if (Number(process.env.GITHUB_RUN_ATTEMPT) <= 1) return;
    const result = await github(
      `actions/runs/${process.env.GITHUB_RUN_ID}/artifacts?per_page=100`,
    );
    if (!result)
      throw new Error("Cannot look up the original release artifacts");
    const artifact = result.artifacts
      .filter(
        (item) =>
          !item.expired &&
          item.name.startsWith(`sdk-release-${process.env.GITHUB_RUN_ID}-`),
      )
      .sort((a, b) => b.id - a.id)[0];
    if (artifact) output("artifact", artifact.name);
    return;
  }
  if (command === "prepare") {
    const source = git(cwd, "rev-parse", "HEAD");
    if (source !== process.env.GITHUB_SHA)
      throw new Error("Checkout does not match the workflow source");
    let plan;
    if (fs.existsSync(path.join(dir, "plan.json"))) {
      plan = JSON.parse(read(dir, "plan.json"));
      validateBundle(dir, plan);
      if (plan.source !== source)
        throw new Error("Saved release belongs to another source commit");
      if (releaseIsPushed(cwd, plan)) {
        output("resumed", true);
      } else {
        plan = null;
      }
    }
    if (!plan) {
      if (
        git(cwd, "ls-remote", "origin", "refs/heads/main").split(/\s/)[0] !==
        source
      ) {
        // A pushed release must resume from its original, tested artifact.
        const notes = git(
          cwd,
          "for-each-ref",
          "--format=%(contents)",
          "refs/tags/npm/",
          "refs/tags/python/",
          "refs/tags/go/",
        );
        if (notes.includes(`\"source\":\"${source}\"`))
          throw new Error(
            "This source was already released; its saved workflow artifact is required for a retry",
          );
        output("stale", true);
        console.log(
          "Main has advanced; its newer workflow will release the changes.",
        );
        return;
      }
      fs.rmSync(dir, { recursive: true, force: true });
      plan = await prepareRelease(cwd, {
        run: `${process.env.GITHUB_SERVER_URL}/${process.env.GITHUB_REPOSITORY}/actions/runs/${process.env.GITHUB_RUN_ID}`,
      });
      fs.mkdirSync(path.join(cwd, "dist"), { recursive: true });
      fs.writeFileSync(
        path.join(cwd, "dist/release-plan.json"),
        JSON.stringify(plan),
      );
    }
    output(
      "artifact",
      process.env.RESTORED_ARTIFACT &&
        fs.existsSync(path.join(dir, "plan.json"))
        ? process.env.RESTORED_ARTIFACT
        : `sdk-release-${process.env.GITHUB_RUN_ID}-${process.env.GITHUB_RUN_ATTEMPT}`,
    );
    output("releasing", plan.releases.length > 0);
    for (const kind of kinds)
      output(
        kind,
        plan.releases.some((release) => release.kind === kind),
      );
    return;
  }
  if (command === "seal") {
    sealRelease(cwd, JSON.parse(read(cwd, "dist/release-plan.json")));
    return;
  }
  const plan = JSON.parse(read(dir, "plan.json"));
  validateBundle(dir, plan);
  if (command === "push") {
    output("ready", pushRelease(cwd, plan));
    return;
  }
  if (!releaseIsPushed(cwd, plan))
    throw new Error("Release tags have not been pushed");
  if (command === "check-publication") {
    const pending = await checkPublication(dir, process.argv[3]);
    output("pending", pending.length);
    return;
  }
  if (command === "finish") {
    // Check every registry before creating any GitHub releases.
    for (const release of plan.releases.filter(({ kind }) => kind !== "go")) {
      const registry = await registryJSON(
        registryURL(release.kind, release.version),
      );
      if (pendingFiles(release.kind, release.files, registry).length)
        throw new Error(
          `Publication incomplete: ${release.tag}; rerun the failed jobs`,
        );
    }
    for (const release of plan.releases) {
      if (await github(`releases/tags/${encodeURIComponent(release.tag)}`))
        continue;
      const notes = await github("releases/generate-notes", {
        tag_name: release.tag,
        ...(release.previous ? { previous_tag_name: release.previous } : {}),
      });
      await github("releases", {
        tag_name: release.tag,
        name: release.tag,
        body: notes.body,
        make_latest: "false",
      });
    }
    return;
  }
  throw new Error(
    "Usage: node scripts/release.mjs dry-run|find-artifact|prepare|seal|push|check-publication <npm|python>|finish",
  );
}

if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href
) {
  await main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
