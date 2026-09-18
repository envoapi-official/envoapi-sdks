import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import YAML from "yaml";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";

test("public snapshot matches its recorded checksum", () => {
  const provenance = JSON.parse(fs.readFileSync("openapi/provenance.json"));
  assert.equal(
    createHash("sha256")
      .update(fs.readFileSync("openapi/public-v1.yaml"))
      .digest("hex"),
    provenance.sha256,
  );
});

test("every operation has a unique resource method in all languages", () => {
  assert.ok(
    fs.existsSync("openapi/operations.json"),
    "operation manifest is missing",
  );
  const manifest = JSON.parse(fs.readFileSync("openapi/operations.json"));
  const spec = YAML.parse(fs.readFileSync("openapi/public-v1.yaml", "utf8"));
  const ids = Object.values(spec.paths)
    .flatMap((p) =>
      Object.values(p)
        .filter((o) => o.operationId)
        .map((o) => o.operationId),
    )
    .sort();
  assert.deepEqual(manifest.map((o) => o.operationId).sort(), ids);
  for (const lang of ["typescript", "python", "go"])
    assert.equal(
      new Set(manifest.map((o) => o.resource + "." + o[lang])).size,
      ids.length,
    );
});

test("regeneration matches checked-in artifacts byte for byte", () => {
  const result = spawnSync(
    process.execPath,
    ["scripts/generate.mjs", "--check"],
    { encoding: "utf8" },
  );
  assert.equal(result.status, 0, result.stdout + result.stderr);
});
