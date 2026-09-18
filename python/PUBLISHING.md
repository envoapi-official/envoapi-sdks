# Publishing the Python SDK

Run commands from the repository root. The Python distribution is `envoapi`, currently version `0.1.0`. Publishing to PyPI is separate from npm publishing and GitHub authentication.

## Prepare and validate (no credentials)

The prepared workspace has the release tools in `.tools/pypi-venv`. To recreate that environment using the locally installed uv:

```sh
.tools/uv-x86_64-unknown-linux-gnu/uv venv .tools/pypi-venv --python .venv/bin/python
.tools/uv-x86_64-unknown-linux-gnu/uv pip install --python .tools/pypi-venv/bin/python build==1.4.0 hatchling==1.29.0 twine==7.0.0
```

On another machine, create a Python 3.11+ virtual environment and install these same tools. The SDK itself does not require these publishing dependencies.

After updating `python/pyproject.toml` and the changelog for a release:

```sh
pnpm verify
.tools/pypi-venv/bin/python -m build python --outdir dist/pypi/0.1.0
.tools/pypi-venv/bin/python -m twine check --strict \
  dist/pypi/0.1.0/envoapi-0.1.0-py3-none-any.whl \
  dist/pypi/0.1.0/envoapi-0.1.0.tar.gz
```

The default build creates a source archive and builds the wheel from that archive, verifying that the source archive contains the files needed to build independently. Release files live in a Python-only version directory, separate from the npm archive. Use a new version and output directory for each release; PyPI does not allow replacing previously uploaded files.

## Create your PyPI token

1. Sign into the intended publishing account at <https://pypi.org/>. Verify its email address and enable two-factor authentication.
2. Open <https://pypi.org/manage/account/token/> and create an API token.
3. For the first upload, select the account-wide scope because the `envoapi` project does not exist under your account yet. The first successful upload creates the project.
4. Keep the token ready to paste at the terminal password prompt. It begins with `pypi-`.

The package's author metadata is `envoapi <envoapi@gmail.com>`. Project ownership on PyPI belongs to the account whose token you use for the first upload. Neither GitHub SSH keys nor npm credentials authenticate PyPI uploads.

## Upload (this publishes publicly)

Only run this step when ready to publish the validated release files:

```sh
.tools/pypi-venv/bin/python -m twine upload \
  --repository-url https://upload.pypi.org/legacy/ \
  --username __token__ \
  dist/pypi/0.1.0/envoapi-0.1.0-py3-none-any.whl \
  dist/pypi/0.1.0/envoapi-0.1.0.tar.gz
```

When Twine prompts for the API token/password, paste the complete token and press Enter. The input is hidden. Do not enter your PyPI website password, put the token in the command, commit it to the repository, or send it in chat. No credentials are needed before this upload step.

After uploading, check <https://pypi.org/project/envoapi/0.1.0/> and install with `python -m pip install envoapi==0.1.0` in a fresh environment. For future uploads, create a token scoped to `envoapi` and revoke the initial account-wide token, or configure PyPI Trusted Publishing.

References: [PyPA packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/), [PyPI API tokens](https://pypi.org/help/#apitoken), [Twine](https://twine.readthedocs.io/en/stable/).
