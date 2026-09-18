# EnvoAPI SDKs

Use EnvoAPI from your TypeScript, JavaScript, Python, or Go project. Look up profiles, companies, posts, jobs, and more with typed clients.

| Language | Install in your project | Guide |
| --- | --- | --- |
| TypeScript / JavaScript (Node.js 22+) | `npm install envoapi` | [npm SDK guide](typescript/README.md) |
| Python 3.11+ | `python -m pip install envoapi` | [Python SDK guide](python/README.md) |
| Go 1.25+ | `go get github.com/envoapi-official/envoapi-sdks/go` | [Go SDK guide](go/README.md) |

## 1. Set your API key

[Get a free API key with 100 credits](https://envoapi.com/envoapi).

Use your EnvoAPI API key as the value of `ENVOAPI_API_KEY`. All three SDKs read this environment variable automatically.

```sh
# macOS / Linux
export ENVOAPI_API_KEY="your-api-key"
```

```powershell
# Windows PowerShell
$env:ENVOAPI_API_KEY="your-api-key"
```

Run your app from the same terminal, or set this variable in your hosting provider's environment settings. Keep the key on your server and out of source control.

## 2. Make a request

These examples get a profile's recent posts. Replace `satyanadella` with the profile username you want to look up.

### TypeScript / JavaScript

```sh
npm install envoapi
```

```javascript
import { EnvoAPI } from 'envoapi';

const client = new EnvoAPI();
const response = await client.profiles.getPosts({ username: 'satyanadella' });

console.log(response.body.data.posts);
console.log(response.body.meta.creditCost);
```

For JavaScript, save this as `app.mjs` and run `node app.mjs`. The same code works in a TypeScript project configured for ES modules. [More examples →](typescript/README.md)

### Python

```sh
python -m pip install envoapi
```

Save as `app.py`:

```python
from envoapi import EnvoAPI

with EnvoAPI() as client:
    response = client.profiles.get_posts(username="satyanadella")
    print(response.body.data.posts)
    print(response.body.meta.credit_cost)
```

Run `python app.py`. An async client is also available. [More examples →](python/README.md)

### Go

From your Go project (run `go mod init example.com/myapp` first if it has no `go.mod`):

```sh
go get github.com/envoapi-official/envoapi-sdks/go
```

Save as `main.go`:

```go
package main

import (
    "context"
    "fmt"
    "log"

    envoapi "github.com/envoapi-official/envoapi-sdks/go"
)

func main() {
    client, err := envoapi.NewClient()
    if err != nil {
        log.Fatal(err)
    }

    response, err := client.Profiles.GetPosts(context.Background(), envoapi.GetProfilePostsParams{
        Username: "satyanadella",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(response.Body.Data.Posts)
    fmt.Println(response.Body.Meta.CreditCost)
}
```

Run `go run .`. [More examples →](go/README.md)

## 3. Explore the API

Each response includes the result in `body.data`, request metadata in `body.meta`, and HTTP status and headers. Go uses `Body.Data` and `Body.Meta`.

See the [method reference](docs/operations.md) for all 52 methods. Each language guide covers passing an API key directly, setting a timeout, and handling errors.

The default API URL is `https://api.envoapi.com`, with a 60-second timeout. The SDKs do not retry requests or fetch additional pages automatically. For paginated methods, pass the returned continuation cursor to the next call. Requests use your EnvoAPI credits.

## Links

- Packages: [npm](https://www.npmjs.com/package/envoapi) · [PyPI](https://pypi.org/project/envoapi/) · [Go documentation](https://pkg.go.dev/github.com/envoapi-official/envoapi-sdks/go)
- [Report an issue](https://github.com/envoapi-official/envoapi-sdks/issues)
- [Contributing and releases](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

## License

[MIT](LICENSE)
