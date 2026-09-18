# EnvoAPI for Python

The EnvoAPI Python SDK provides typed synchronous and asynchronous clients for all 52 public API operations, using HTTPX transports. Requires Python 3.11+.

## Installation

```sh
pip install envoapi
```

## Authentication and synchronous requests

Set `ENVOAPI_API_KEY` to your EnvoAPI API key, or pass `api_key` when creating the client. This is the API key for EnvoAPI requests, separate from credentials used to publish packages to PyPI.

```python
from envoapi import EnvoAPI, APIError

with EnvoAPI() as client:  # reads ENVOAPI_API_KEY
    response = client.profiles.get_details_by_username(username="alice")
    print(response.body.data, response.body.meta.credit_cost)
    print(response.headers.get("x-request-id"))
```

## Asynchronous requests

```python
import asyncio
from envoapi import AsyncEnvoAPI

async def lookup():
    async with AsyncEnvoAPI() as client:
        response = await client.profiles.get_posts(username="alice")
        return response.body.data.posts

posts = asyncio.run(lookup())
print(posts)
```

## Configuration and responses

Configure `api_key`, `base_url`, `timeout` (seconds or `httpx.Timeout`), and `transport` on either client. Context managers close their owned HTTPX client and transport; manual callers must use `close()` / `await aclose()`. Cancellation of an async task propagates unchanged. Methods make one request with no retries or automatic pagination.

The default base URL is `https://api.envoapi.com` and the default timeout is 60 seconds per HTTPX timeout phase. For pagination, pass the response's continuation cursor to the next request explicitly. Repeated requests can incur additional charges.

The response exposes `body`, `status`, and `headers`. Models use snake_case attributes and provide `to_dict()` for wire-format serialization. `from envoapi import models` exposes generated models and parameter enums; `UNSET` distinguishes omitted optional values from `None`. Date-time fields become Python datetimes, so serialization can normalize an equivalent UTC timestamp.

`APIError` exposes `status`, `code`, `retryable`, `request_id`, `headers`, and `body`. Transport failures retain the original exception in `__cause__`. `DecodeError` indicates a malformed successful response.

See the [operation reference](https://github.com/envoapi-official/envoapi-sdks/blob/main/docs/operations.md) for every resource method and the [repository](https://github.com/envoapi-official/envoapi-sdks) for development instructions. Maintainers can follow the [PyPI release instructions](https://github.com/envoapi-official/envoapi-sdks/blob/main/python/PUBLISHING.md).
