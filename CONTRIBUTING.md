# Contributing

These instructions are for working on the SDKs. To use EnvoAPI in your project, start with the [README](README.md).

## Development setup

Use Node.js 22+, pnpm 11.10.0, Python 3.11+, Go 1.25+, uv, and a C compiler for Go's race detector. Scripts use tools on PATH, or local toolchains in `.venv` and `.tools`. Set `CC` if Go needs a specific C compiler.

```sh
pnpm install --frozen-lockfile
uv venv .venv --python 3.11
uv pip sync --python .venv/bin/python requirements-dev.lock
pnpm verify
```

Verification generates into temporary storage, checks drift and endpoint coverage, runs behavior and type tests, builds packages, and installs them into separate consumer projects. Package installation may download public dependencies; no private credentials or live API calls are needed.

```sh
pnpm generate                          # regenerate all three SDKs
pnpm generate:check                    # compare without rewriting tracked files
pnpm contract:import ~/envoapi-backend # explicitly import a committed public snapshot
pnpm verify                            # full local acceptance checks
```

The import records the source commit and SHA-256 checksum in `openapi/provenance.json`. It refuses an uncommitted contract or external references. Review the snapshot, regenerate, and verify together when updating. The source backend is never modified.

## Updating and releasing SDKs

TypeScript uses `openapi-typescript` and `openapi-fetch`. Python uses `openapi-python-client` with a small documented [template adaptation](python/templates/README.md). Go uses `oapi-codegen` v2.8.0. Versions and dependencies are pinned in the package lockfiles, Python development lock, and Go module files.

The canonical snapshot is copied byte for byte. Synthetic fixtures test serialization shape, metadata, and union branches; they are not valid selectors for live lookup requests. The SDK does not add endpoints merely because related schemas appear in the document.

See the [Python release instructions](python/PUBLISHING.md) for building, checking, and uploading the PyPI distribution. Publishing automation is deferred. Future Go tags must include the module subdirectory, for example `go/v0.1.0`; each language can release independently. Future Actions jobs must use runner group `envoapi-runner` and labels `[self-hosted, linux, x64]`.

## Working on Go locally

To test local changes from another Go module:

```sh
go mod edit -require=github.com/envoapi-official/envoapi-sdks/go@v0.0.0
go mod edit -replace=github.com/envoapi-official/envoapi-sdks/go=/absolute/path/to/envoapi-sdks/go
go mod tidy
```

Release tags use the `go/` prefix, for example `go/v0.1.0`, because this module is in the repository's `go/` subdirectory. The repository must be public for unauthenticated installation through the public Go proxy. Go releases do not require a separate registry account or package upload.

## License files

Keep `LICENSE`, `typescript/LICENSE`, `python/LICENSE`, and `go/LICENSE` identical. The vendored Python generator template retains its original copyright notice in `python/templates/LICENSE`.
