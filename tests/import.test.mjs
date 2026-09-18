import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";

test("contract import records an exact committed snapshot and refuses dirty input", () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "envoapi-import-test-"));
  try {
    const source = path.join(tmp, "backend"),
      output = path.join(tmp, "output");
    const contract = path.join(
      source,
      "packages/contracts/openapi/public-v1.yaml",
    );
    fs.mkdirSync(path.dirname(contract), { recursive: true });
    const yaml =
      "openapi: 3.1.0\ninfo: {title: Test, version: v1}\npaths: {}\n";
    fs.writeFileSync(contract, yaml);
    for (const args of [
      ["init", "-q"],
      ["add", "."],
      [
        "-c",
        "user.name=SDK Test",
        "-c",
        "user.email=sdk@example.invalid",
        "commit",
        "-qm",
        "snapshot",
      ],
    ]) {
      const r = spawnSync("git", args, { cwd: source });
      assert.equal(r.status, 0);
    }
    const result = spawnSync(
      process.execPath,
      ["scripts/import-contract.mjs", source, "--output", output],
      { encoding: "utf8" },
    );
    assert.equal(result.status, 0, result.stderr);
    assert.equal(
      fs.readFileSync(path.join(output, "public-v1.yaml"), "utf8"),
      yaml,
    );
    const provenance = JSON.parse(
      fs.readFileSync(path.join(output, "provenance.json")),
    );
    assert.equal(
      provenance.sha256,
      createHash("sha256").update(yaml).digest("hex"),
    );
    assert.equal(
      provenance.commit,
      spawnSync("git", ["rev-parse", "HEAD"], {
        cwd: source,
        encoding: "utf8",
      }).stdout.trim(),
    );
    fs.appendFileSync(contract, "# local changes\n");
    const dirty = spawnSync(
      process.execPath,
      ["scripts/import-contract.mjs", source, "--output", output],
      { encoding: "utf8" },
    );
    assert.notEqual(dirty.status, 0);
    assert.match(dirty.stderr, /uncommitted/i);
    assert.equal(
      fs.readFileSync(path.join(output, "public-v1.yaml"), "utf8"),
      yaml,
    );
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
});
