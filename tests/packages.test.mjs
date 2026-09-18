import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";

test("packaged SDKs run in independent consumer projects against a local server", () => {
  const result = spawnSync(process.execPath, ["scripts/package-smoke.mjs"], {
    encoding: "utf8",
    timeout: 240000,
  });
  assert.equal(result.status, 0, result.stdout + result.stderr);
});
