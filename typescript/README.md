# EnvoAPI for TypeScript and JavaScript

Requires Node.js 22+. This is an ESM package, currently available for local installation only.

From the repository root:

```sh
pnpm --filter envoapi build
pnpm --dir typescript pack --pack-destination ../dist
# In another project:
pnpm add /absolute/path/to/envoapi-sdks/dist/envoapi-0.1.1.tgz
```

```typescript
import { EnvoAPI, APIError } from 'envoapi';

const client = new EnvoAPI({ timeoutMs: 60_000 }); // reads ENVOAPI_API_KEY
try {
  const result = await client.profiles.getDetailsByUsername({ username: 'alice' });
  console.log(result.body.data, result.body.meta, result.headers.get('x-request-id'));
} catch (error) {
  if (error instanceof APIError) console.error(error.status, error.code, error.requestId);
  else throw error;
}
```

Configure `apiKey`, `baseUrl`, `timeoutMs`, or `fetch` on the client. Supply `{ signal }` as a resource method's second argument for cancellation. All methods make a single request; pass pagination query parameters explicitly. Types are exported as `components`, `operations`, and `paths`, along with the SDK response, configuration, and error types.
