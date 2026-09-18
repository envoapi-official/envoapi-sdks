import path from "node:path";
import fs from "node:fs";
import { fileURLToPath } from "node:url";
export const root = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "..",
);
export const env = {
  ...process.env,
  PATH: [
    path.join(root, ".venv/bin"),
    path.join(root, ".tools/go/bin"),
    path.join(root, ".tools/uv-x86_64-unknown-linux-gnu"),
    process.env.PATH,
  ].join(path.delimiter),
  PYTHONPATH: path.join(root, "python"),
  CC:
    process.env.CC ??
    (fs.existsSync(path.join(root, ".tools/cc"))
      ? path.join(root, ".tools/cc")
      : "cc"),
};
