// Synthetic values for exercising generated parsers. Not live API request examples.
import fs from "node:fs";
import YAML from "yaml";
const spec = YAML.parse(fs.readFileSync("openapi/public-v1.yaml", "utf8"));
function sample(schema, depth = 0) {
  if (depth > 50) throw new Error("Recursive schema needs an explicit fixture");
  if (schema.$ref)
    return sample(
      spec.components.schemas[schema.$ref.split("/").at(-1)],
      depth + 1,
    );
  if ("const" in schema) return schema.const;
  if (schema.enum) return schema.enum[0];
  if (schema.anyOf || schema.oneOf) {
    const branches = schema.anyOf ?? schema.oneOf;
    const value = sample(
      branches.find((b) => b.type === "null") ?? branches[0],
      depth + 1,
    );
    if (schema.properties) {
      const { anyOf, oneOf, ...base } = schema;
      return { ...sample(base, depth + 1), ...value };
    }
    return value;
  }
  if (schema.type === "null") return null;
  if (schema.type === "object" || schema.properties)
    return Object.fromEntries(
      Object.entries(schema.properties ?? {}).map(([key, s]) => [
        key,
        sample(s, depth + 1),
      ]),
    );
  if (schema.type === "array") return [sample(schema.items, depth + 1)];
  if (schema.type === "boolean") return false;
  if (schema.type === "number" || schema.type === "integer")
    return schema.minimum ?? 0;
  if (schema.type === "string") {
    if (schema.format === "date-time") return "2026-01-01T00:00:00Z";
    if (schema.format === "date") return "2026-01-01";
    if (schema.format === "uri") return "https://example.invalid/sample";
    return "sample";
  }
  if (schema.not?.type === "null") return "sample";
  if (schema.not) return {};
  throw new Error("Unhandled fixture schema " + JSON.stringify(schema));
}
const operations = {};
for (const [route, item] of Object.entries(spec.paths)) {
  const op = item.get;
  const query = Object.fromEntries(
    op.parameters
      .filter((p) => p.required)
      .map((p) => [p.name, sample(p.schema)]),
  );
  operations[op.operationId] = {
    path: route,
    query,
    response: sample(op.responses["200"].content["application/json"].schema),
  };
}
fs.writeFileSync(
  "tests/fixtures/operations.json",
  JSON.stringify(operations, null, 2) + "\n",
);
