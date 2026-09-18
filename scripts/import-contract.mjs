import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import YAML from "yaml";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const source = process.argv[2];
if (!source)
  throw new Error("Usage: pnpm contract:import /path/to/envoapi-backend");
const relative = "packages/contracts/openapi/public-v1.yaml";
const git = (args) => {
  const r = spawnSync("git", ["-C", source, ...args], { encoding: "utf8" });
  if (r.status !== 0) throw new Error(r.stderr);
  return r.stdout.trim();
};
git(["ls-files", "--error-unmatch", relative]);
if (git(["status", "--porcelain", "--", relative]))
  throw new Error(
    "Public contract has uncommitted changes; commit it before importing.",
  );
const commit = git(["rev-parse", "HEAD"]);
const bytes = fs.readFileSync(path.join(source, relative));
const spec = YAML.parse(bytes.toString());
if (!spec.openapi?.startsWith("3.1.") || !spec.paths)
  throw new Error("Expected a public OpenAPI 3.1 document");
function check(value) {
  if (!value || typeof value !== "object") return;
  if (value.$ref && !value.$ref.startsWith("#/"))
    throw new Error("Contract must be standalone: external reference found");
  Object.values(value).forEach(check);
}
check(spec);
const index = process.argv.indexOf("--output");
const dest =
  index === -1
    ? path.join(root, "openapi")
    : path.resolve(process.argv[index + 1]);
const provenance = {
  source: "envoapi-backend/" + relative,
  commit,
  sha256: createHash("sha256").update(bytes).digest("hex"),
};
fs.mkdirSync(dest, { recursive: true });
fs.writeFileSync(path.join(dest, "public-v1.yaml"), bytes);
fs.writeFileSync(
  path.join(dest, "provenance.json"),
  JSON.stringify(provenance, null, 2) + "\n",
);
console.log(
  `Imported public contract from ${commit}. Run pnpm generate and pnpm verify.`,
);
