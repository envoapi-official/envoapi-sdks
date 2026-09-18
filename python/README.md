# EnvoAPI for Python

Call EnvoAPI from your Python app to look up profiles, companies, posts, jobs, and more. Includes typed sync and async clients.

Requires **Python 3.11+**.

## Install

```sh
python -m pip install envoapi
```

## Set your API key

[Get a free API key with 100 credits](https://envoapi.com/signup).

Pass your key directly with `EnvoAPI(api_key="your-api-key")` or `AsyncEnvoAPI(api_key="your-api-key")`. **The `ENVOAPI_API_KEY` environment variable is optional.** An explicitly supplied key takes precedence.

Alternatively, set the environment variable and omit `api_key`:

```sh
# macOS / Linux
export ENVOAPI_API_KEY="your-api-key"
```

```powershell
# Windows PowerShell
$env:ENVOAPI_API_KEY="your-api-key"
```

If you use the environment variable, run your app from the same terminal. Both clients read it automatically when `api_key` is omitted. Keep your key out of source control.

## Make a request

Save as `app.py`:

```python
from envoapi import EnvoAPI

with EnvoAPI(api_key="your-api-key") as client:
    response = client.profiles.get_posts(username="satyanadella")
    print(response.body.data.posts)
    print(response.body.meta.credit_cost)
```

Run it:

```sh
python app.py
```

Replace `satyanadella` with the profile username you want to look up. The `with` block closes the client when you are done.

## Async requests

```python
import asyncio
from envoapi import AsyncEnvoAPI

async def main():
    async with AsyncEnvoAPI(api_key="your-api-key") as client:
        response = await client.profiles.get_posts(username="satyanadella")
        print(response.body.data.posts)

asyncio.run(main())
```

In an app that already has an event loop, use `await` inside your async function instead of calling `asyncio.run()`.

## Client options

You can also pass a key from your app's configuration. An explicit key overrides `ENVOAPI_API_KEY`.

```python
from envoapi import EnvoAPI

with EnvoAPI(api_key="your-api-key", timeout=30.0) as client:
    response = client.profiles.get_posts(username="satyanadella")
    print(response.body.data.posts)
```

Both clients accept the same options. The default timeout is 60 seconds per HTTPX timeout phase; `timeout` accepts seconds or `httpx.Timeout`. Use `base_url` to change the default `https://api.envoapi.com`, or `transport` for a custom HTTPX transport.

## Handle errors

```python
from envoapi import APIError, EnvoAPI

try:
    with EnvoAPI(api_key="your-api-key") as client:
        response = client.profiles.get_posts(username="satyanadella")
        print(response.body.data.posts)
except APIError as error:
    print(error.status, error.code, str(error), error.request_id)
```

`APIError` means the API returned an error. `TransportError` means the request failed, and `DecodeError` means the response could not be read in the expected format. All three can be imported from `envoapi`.

## Responses and more methods

- `response.body.data`: the result.
- `response.body.meta`: request metadata, including `credit_cost`.
- `response.status` and `response.headers`: HTTP status and headers.
- `response.body.to_dict()`: the response body as a dictionary.

Model attributes use snake_case. The SDK does not retry requests or fetch additional pages automatically. For paginated methods, pass the returned continuation cursor to the next call with the same search parameters. Requests use your EnvoAPI credits.

See the [method reference](https://github.com/envoapi-official/envoapi-sdks/blob/main/docs/operations.md) for all available calls. For models and enums, use `from envoapi import models`.

[GitHub](https://github.com/envoapi-official/envoapi-sdks) · [Issues](https://github.com/envoapi-official/envoapi-sdks/issues) · [MIT license](https://github.com/envoapi-official/envoapi-sdks/blob/main/LICENSE)
