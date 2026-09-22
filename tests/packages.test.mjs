import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import { readVersions } from "../scripts/release.mjs";

test("packaged SDKs run in independent consumer projects against a local server", () => {
  const result = spawnSync(process.execPath, ["scripts/package-smoke.mjs"], {
    encoding: "utf8",
    timeout: 240000,
  });
  assert.equal(result.status, 0, result.stdout + result.stderr);
  const versions = readVersions(process.cwd());
  assert.deepEqual(fs.readdirSync("dist/packages/npm"), [
    `envoapi-${versions.npm}.tgz`,
  ]);
  assert.deepEqual(
    fs.readdirSync("dist/packages/python").sort(),
    [
      `envoapi-${versions.python}-py3-none-any.whl`,
      `envoapi-${versions.python}.tar.gz`,
    ].sort(),
  );
});
