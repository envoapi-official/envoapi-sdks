# EnvoAPI SDKs

SDK repository for TypeScript/JavaScript, Python, and Go. All three clients cover the 52 operations in the committed public OpenAPI 3.1 snapshot. Builds and installed clients do not depend on the backend repository or its private contracts package.

The packages are versioned `0.1.0`. The TypeScript/JavaScript SDK is published on npm as `envoapi`; the Python SDK is being prepared for PyPI under the same name. The repository is `envoapi-official/envoapi-sdks`, and the Go module is `github.com/envoapi-official/envoapi-sdks/go`.

## Local development

Use Node.js 22+, pnpm 11.10.0, Python 3.11+, Go 1.25+, uv, and a C compiler for Go's race detector. The current workspace has Python in `.venv`, Go in `.tools/go`, uv in `.tools/uv-x86_64-unknown-linux-gnu`, and a local Zig C compiler wrapper in `.tools/cc`. Scripts automatically find these local toolchains; on other machines they use the tools on PATH and the optional `CC` setting.

```sh
pnpm install --frozen-lockfile
uv venv .venv --python 3.11
uv pip sync --python .venv/bin/python requirements-dev.lock
pnpm verify
```

On this prepared workspace, run `pnpm verify` directly. Verification generates into temporary storage, checks drift and endpoint coverage, runs behavior and type tests, builds packages, and installs them into separate consumer projects. Package installation may download public dependencies; no private credentials or live API calls are needed.

```sh
pnpm generate                          # regenerate all three SDKs
pnpm generate:check                    # compare without rewriting tracked files
pnpm contract:import ~/envoapi-backend # explicitly import a committed public snapshot
pnpm verify                            # full local acceptance checks
```

The import records the source commit and SHA-256 checksum in `openapi/provenance.json`. It refuses an uncommitted contract or external references. Review the snapshot, regenerate, and verify together when updating. The source backend is never modified.

## Clients

```javascript
import { EnvoAPI } from 'envoapi';
const client = new EnvoAPI(); // ENVOAPI_API_KEY
const response = await client.profiles.getPosts({ username: 'alice' });
console.log(response.body.data.posts, response.body.meta.creditCost);
```

```python
from envoapi import EnvoAPI

with EnvoAPI() as client:
    response = client.profiles.get_posts(username="alice")
    print(response.body.data.posts, response.body.meta.credit_cost)
```

```go
client, err := envoapi.NewClient() // ENVOAPI_API_KEY
if err != nil { log.Fatal(err) }
response, err := client.Profiles.GetPosts(ctx, envoapi.GetProfilePostsParams{Username: "alice"})
if err != nil { log.Fatal(err) }
fmt.Println(response.Body.Data.Posts, response.Body.Meta.CreditCost)
```

Each method returns a response containing the typed API envelope (`body` / `Body`), HTTP status, and headers. Python models use snake_case attributes; `to_dict()` restores wire names. Go models and enums are available in the public `api` subpackage. [Every resource method](docs/operations.md) maps to one contract operation, including separate URL, username, slug, and ID variants.

- An explicit API key overrides `ENVOAPI_API_KEY`; missing or blank keys fail before sending a request.
- The default base URL is `https://api.envoapi.com`. Override it for a local server or testing.
- Requests default to a 60-second timeout. TypeScript and Go apply a whole-request deadline; Python uses HTTPX's connect/read/write/pool timeouts, configurable with `httpx.Timeout`.
- There are no SDK retries or automatic pagination. Pass the returned continuation cursor explicitly. A repeated request can incur another charge, and cancellation does not imply a refund.
- TypeScript accepts `AbortSignal`, Python async calls support task cancellation, and Go methods take `context.Context`.
- `APIError` preserves HTTP status, backend code, retryability, request ID, headers, and the response body. `TransportError` wraps network failures; `DecodeError` identifies an invalid successful response. Non-JSON HTTP failures remain API errors.
- The SDKs preserve known contract fields and nullable/union variants. They do not perform exhaustive JSON Schema validation of responses. Regenerate the clients when the contract changes.
- Default clients do not follow redirects. Injected transports remain under the caller's control, including any retry or redirect policy they implement.

See the language READMEs and `examples/` for local installation and runnable examples. Examples make real, potentially billable requests when pointed at the public API; the verification suite runs them against a local stub.

## Generation and release notes

TypeScript uses `openapi-typescript` and `openapi-fetch`. Python uses `openapi-python-client` with a small documented [template adaptation](python/templates/README.md). Go uses `oapi-codegen` v2.8.0. Versions and dependencies are pinned in the package lockfiles, Python development lock, and Go module files.

The canonical snapshot is copied byte for byte. Synthetic fixtures test serialization shape, metadata, and union branches; they are not valid selectors for live lookup requests. The SDK does not add endpoints merely because related schemas appear in the document.

See the [Python release instructions](python/PUBLISHING.md) for building, checking, and uploading the PyPI distribution. Publishing automation is deferred. Future Go tags must include the module subdirectory, for example `go/v0.1.0`; each language can release independently. Future Actions jobs must use runner group `envoapi-runner` and labels `[self-hosted, linux, x64]`.
