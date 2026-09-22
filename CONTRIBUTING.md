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

Pull requests to `main` run `pnpm verify`. Each push to `main` runs verification and automatically releases changed SDKs. No release PR, commit-message convention, or manual tag is needed.

Each SDK gets its own patch increment and tag: `npm/vX.Y.Z`, `python/vX.Y.Z`, and `go/vX.Y.Z`. Changes under `typescript/`, `python/`, or `go/` release that SDK, including its packaged documentation. Changes to `openapi/`, `scripts/`, root package manifests, lockfiles, or `LICENSE` release all three. Root documentation, `examples/`, `tests/`, and `.github/` changes run CI without publishing. Each comparison starts at that SDK's latest release tag, so queued updates are included in the next release.

For a minor or major release, set a higher version in the PR: TypeScript's `package.json` and runtime user-agent, Python's `pyproject.toml` and runtime user-agent, or Go's `sdkVersion` in `client.go`. The higher version overrides the patch increment. Versions must be stable `X.Y.Z`; downgrades and prereleases are rejected. Go v2+ needs a separate module-path migration before this workflow can publish it.

The workflow stamps versions before verification, saves the tested npm archive and Python wheel/source archive, and pushes the version commit plus all selected tags atomically. A newer `main` prevents a stale push. Releases run one at a time and are never cancelled by a newer push; GitHub may replace a queued run with the newest one. The automatic version commit uses `GITHUB_TOKEN`, so it does not trigger another run. Go becomes available from its tag. GitHub release notes are generated after npm and PyPI publication succeeds; see [Releases](https://github.com/envoapi-official/envoapi-sdks/releases).

### One-time setup

No repository secrets or variables are required. GitHub provides `GITHUB_TOKEN` and OIDC credentials automatically.

1. Repository rules must allow the workflow token to write the version commit to `main` and create SDK tags. If rules require PRs for every commit, configure an allowed automation bypass before enabling releases. All jobs use GitHub-hosted `ubuntu-latest` runners; no runner group or self-hosted runner setup is required.
2. In the npm **envoapi** package settings, add a GitHub Actions trusted publisher: owner **envoapi-official**, repository **envoapi-sdks**, workflow **release.yml**, environment **leave blank**. Enable direct publishing for this publisher.
3. In the PyPI **envoapi** project's Publishing settings, add the same GitHub owner, repository, and workflow; leave the environment blank. See [Python publishing](python/PUBLISHING.md).

Workflows install Node.js, pnpm, Python, Go, and uv on GitHub-hosted runners. npm and PyPI uploads use `id-token: write` for trusted publishing. Both workflows pin third-party actions to commit hashes. References: [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/), [PyPI trusted publishers](https://docs.pypi.org/trusted-publishers/adding-a-publisher/), [GitHub token-triggered events](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow#triggering-a-workflow-from-a-workflow).

### Preview and recovery

After installing development dependencies, preview the next release:

```sh
pnpm release:dry-run
```

This includes your local edits in a temporary checkout, calculates versions using local tags and public registry metadata, and runs the complete verification against the staged versions. It prints the versions and archive hashes, then removes the temporary checkout. Your source files, index, branches, tags, and existing distribution files are preserved. Fetch current tags first when previewing from an older checkout.

If publication fails, open the **original Release workflow run** and choose **Re-run failed jobs**. Re-running all jobs also restores that run's saved artifact. Retries verify the remote tags and archive hashes, skip identical files already published, and upload only missing files. They neither rebuild published packages nor bump versions again. The final publication check and release-note creation retry up to six times, 30 seconds apart, to tolerate registry propagation delays. A newer release is blocked while the latest tagged npm or Python version has missing files. Recover the failed release first, then rerun the latest main workflow.

Artifacts are retained for 90 days, subject to repository retention limits. If the original artifact is missing, restore the exact files from a backup before recovery. A conflicting existing tag or registry file stops the workflow and requires investigation; do not delete/reuse published versions or move tags. npm publishing also refuses to move `latest` backwards. Registry outages and permission errors fail the run instead of being treated as missing versions.

On the first automated release, npm and Python bootstrap from their currently published versions because historical releases have no SDK tags. Existing Go tags remain the Go baseline.

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
