# EnvoAPI for Python

Requires Python 3.11+. Provides typed synchronous and asynchronous clients, with HTTPX transports. The package is currently available for local installation only.

```sh
# From the repository root, after installing development dependencies:
.venv/bin/python -m build --wheel python --outdir dist
# In another environment:
uv pip install /absolute/path/to/envoapi-sdks/dist/envoapi-0.1.0-py3-none-any.whl
```

```python
from envoapi import EnvoAPI, APIError

with EnvoAPI() as client:  # reads ENVOAPI_API_KEY
    response = client.profiles.get_details_by_username(username="alice")
    print(response.body.data, response.body.meta.credit_cost)
    print(response.headers.get("x-request-id"))
```

```python
from envoapi import AsyncEnvoAPI

async def lookup():
    async with AsyncEnvoAPI() as client:
        response = await client.profiles.get_posts(username="alice")
        return response.body.data.posts
```

Configure `api_key`, `base_url`, `timeout` (seconds or `httpx.Timeout`), and `transport` on either client. Context managers close their owned HTTPX client and transport; manual callers must use `close()` / `await aclose()`. Cancellation of an async task propagates unchanged. Methods make one request with no retries or automatic pagination.

The response exposes `body`, `status`, and `headers`. Models use snake_case attributes and provide `to_dict()` for wire-format serialization. `from envoapi import models` exposes generated models and parameter enums; `UNSET` distinguishes omitted optional values from `None`. Date-time fields become Python datetimes, so serialization can normalize an equivalent UTC timestamp.

`APIError` exposes `status`, `code`, `retryable`, `request_id`, `headers`, and `body`. Transport failures retain the original exception in `__cause__`. `DecodeError` indicates a malformed successful response.
