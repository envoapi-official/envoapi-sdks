# Publishing the Python SDK

Updates to `main` are verified and published automatically by [release.yml](../.github/workflows/release.yml). The PyPI package name is **envoapi**. Releases use tags such as `python/v0.1.3` and appear in [GitHub Releases](https://github.com/envoapi-official/envoapi-sdks/releases).

## One-time PyPI setup

In the existing [envoapi project's Publishing settings](https://pypi.org/manage/project/envoapi/settings/publishing/), add a GitHub Actions trusted publisher:

| Field             | Value              |
| ----------------- | ------------------ |
| Owner             | `envoapi-official` |
| Repository        | `envoapi-sdks`     |
| Workflow filename | `release.yml`      |
| Environment       | Leave blank        |

Use an account with publishing access to the existing project. No API token, repository secret, or environment variable is needed. The hosted publishing job gets a short-lived credential through OIDC. See [PyPI's setup instructions](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

## What gets published

The release workflow updates `pyproject.toml` and the runtime user-agent before running `pnpm verify`. Verification builds a source archive and then builds the wheel from that archive. It installs that wheel into a separate consumer environment and exercises both synchronous and asynchronous clients.

The tested files are `dist/packages/python/envoapi-X.Y.Z.tar.gz` and `dist/packages/python/envoapi-X.Y.Z-py3-none-any.whl`. Only these Python files are passed to the PyPI action. Their SHA-256 hashes are saved in the workflow artifact and annotated release tag.

Patch versions increment automatically for Python or shared build/contract changes. Set a higher stable version in `pyproject.toml` and the runtime user-agent in your PR to request a minor or major release. Preview locally with `pnpm release:dry-run` after the [development setup](../CONTRIBUTING.md#development-setup).

If an upload is interrupted, choose **Re-run failed jobs** on the original Release workflow run. The workflow reuses its saved files, checks PyPI hashes, and uploads only missing distributions. It stops if a published filename has different contents. Never rebuild and overwrite an already published version. See [release recovery](../CONTRIBUTING.md#preview-and-recovery) for artifact retention and recovery details.
