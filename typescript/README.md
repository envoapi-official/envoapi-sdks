# EnvoAPI for TypeScript and JavaScript

Call EnvoAPI from your Node.js app to look up profiles, companies, posts, jobs, and more. TypeScript types are included.

Requires **Node.js 22+**. This package uses ES modules (`import`). Use it in server-side code so your API key stays private.

## Install

```sh
npm install envoapi
```

Or use `pnpm add envoapi` or `yarn add envoapi`.

## Set your API key

[Get a free API key with 100 credits](https://envoapi.com/envoapi).

```sh
# macOS / Linux
export ENVOAPI_API_KEY="your-api-key"
```

```powershell
# Windows PowerShell
$env:ENVOAPI_API_KEY="your-api-key"
```

Run your app from the same terminal. `new EnvoAPI()` reads this variable automatically.

## Make a request

Save as `app.mjs`:

```javascript
import { EnvoAPI } from 'envoapi';

const client = new EnvoAPI();
const response = await client.profiles.getPosts({ username: 'satyanadella' });

console.log(response.body.data.posts);
console.log(response.body.meta.creditCost);
```

Run it:

```sh
node app.mjs
```

Replace `satyanadella` with the profile username you want to look up. For `.js` files, set `"type": "module"` in your project's `package.json`.

In a TypeScript project configured for ES modules, use the same import and calls. Parameters and responses are typed automatically:

```typescript
import { EnvoAPI } from 'envoapi';

const client = new EnvoAPI();

async function getPosts(username: string) {
  const response = await client.profiles.getPosts({ username });
  return response.body.data.posts;
}

console.log(await getPosts('satyanadella'));
```

## Client options

You can also pass a key from your app's configuration. An explicit key overrides `ENVOAPI_API_KEY`.

```javascript
const client = new EnvoAPI({
  apiKey: process.env.ENVOAPI_API_KEY,
  timeoutMs: 30_000,
});
```

The default timeout is 60 seconds. Use `baseUrl` to change the default `https://api.envoapi.com`, or `fetch` to provide a custom transport. To cancel a request, pass `{ signal }` as the method's second argument.

## Handle errors

```javascript
import { EnvoAPI, APIError } from 'envoapi';

const client = new EnvoAPI();

try {
  const response = await client.profiles.getPosts({ username: 'satyanadella' });
  console.log(response.body.data.posts);
} catch (error) {
  if (error instanceof APIError) {
    console.error(error.status, error.code, error.message, error.requestId);
  } else {
    throw error;
  }
}
```

`APIError` means the API returned an error. `TransportError` means the request failed, and `DecodeError` means the response could not be read in the expected format. All three are exported from `envoapi`.

## Responses and more methods

- `response.body.data`: the result.
- `response.body.meta`: request metadata, including `creditCost`.
- `response.status` and `response.headers`: HTTP status and headers.

The SDK does not retry requests or fetch additional pages automatically. For paginated methods, pass the returned continuation cursor to the next call with the same search parameters. Requests use your EnvoAPI credits.

See the [method reference](https://github.com/envoapi-official/envoapi-sdks/blob/main/docs/operations.md) for all available calls. For advanced TypeScript use, schema types are exported as `components`, `operations`, and `paths`.

[GitHub](https://github.com/envoapi-official/envoapi-sdks) · [Issues](https://github.com/envoapi-official/envoapi-sdks/issues) · [MIT license](https://github.com/envoapi-official/envoapi-sdks/blob/main/LICENSE)
