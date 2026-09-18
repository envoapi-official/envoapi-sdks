# EnvoAPI for Go

Call EnvoAPI from your Go app to look up profiles, companies, posts, jobs, and more.

Requires **Go 1.25+**.

## Install

Run this in your Go project:

```sh
go get github.com/envoapi-official/envoapi-sdks/go
```

For a new project, run `go mod init example.com/myapp` first.

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

Run your app from the same terminal. `envoapi.NewClient()` reads this variable automatically. Keep your key out of source control.

## Make a request

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

Run it:

```sh
go run .
```

Replace `satyanadella` with the profile username you want to look up. In an HTTP handler, pass `r.Context()` so the request can be cancelled when the caller disconnects.

## Client options

You can also pass a key from your app's configuration. An explicit key overrides `ENVOAPI_API_KEY`.

```go
// Add "os" and "time" to your imports. Use this inside your function.
client, err := envoapi.NewClient(
    envoapi.WithAPIKey(os.Getenv("ENVOAPI_API_KEY")),
    envoapi.WithTimeout(30*time.Second),
)
if err != nil {
    log.Fatal(err)
}
```

The default timeout is 60 seconds. Use `WithBaseURL` to change the default `https://api.envoapi.com`, or `WithHTTPClient` to provide a custom HTTP client.

## Handle errors

Replace the request and its error check with this block. Add `"errors"` to your imports.

```go
response, err := client.Profiles.GetPosts(context.Background(), envoapi.GetProfilePostsParams{
    Username: "satyanadella",
})
if err != nil {
    var apiErr *envoapi.APIError
    if errors.As(err, &apiErr) {
        log.Printf("status=%d code=%s message=%s request_id=%s",
            apiErr.Status, apiErr.Code, apiErr.Message, apiErr.RequestID)
    } else {
        log.Print(err)
    }
    return
}
fmt.Println(response.Body.Data.Posts)
```

`APIError` means the API returned an error. `TransportError` means the request failed, and `DecodeError` means the response could not be read in the expected format.

## Responses and more methods

- `response.Body.Data`: the result.
- `response.Body.Meta`: request metadata, including `CreditCost`.
- `response.Status` and `response.Headers`: HTTP status and headers.

The SDK does not retry requests or fetch additional pages automatically. For paginated methods, pass the returned continuation cursor to the next call with the same search parameters. Requests use your EnvoAPI credits.

See the [method reference](https://github.com/envoapi-official/envoapi-sdks/blob/main/docs/operations.md) or [Go API documentation](https://pkg.go.dev/github.com/envoapi-official/envoapi-sdks/go) for more calls. Models and enums are in the `github.com/envoapi-official/envoapi-sdks/go/api` package.

[GitHub](https://github.com/envoapi-official/envoapi-sdks) · [Issues](https://github.com/envoapi-official/envoapi-sdks/issues) · [MIT license](https://github.com/envoapi-official/envoapi-sdks/blob/main/LICENSE)
