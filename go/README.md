# EnvoAPI for Go

Module: `github.com/envoapi-official/envoapi-sdks/go`. Requires Go 1.25+.

## Installation

```sh
# In your consumer module:
go get github.com/envoapi-official/envoapi-sdks/go@v0.1.1
```

## Usage

```go
import (
    "context"
    "github.com/envoapi-official/envoapi-sdks/go"
)

func lookup(ctx context.Context) error {
    client, err := envoapi.NewClient() // ENVOAPI_API_KEY
    if err != nil { return err }
    response, err := client.Profiles.GetPosts(ctx, envoapi.GetProfilePostsParams{Username: "alice"})
    if err != nil { return err }
    _ = response.Body.Data.Posts
    _ = response.Headers.Get("X-Request-Id")
    return nil
}
```

Options: `WithAPIKey`, `WithBaseURL`, `WithTimeout`, and `WithHTTPClient`. Every method takes a context and a typed parameter struct. Methods make one request without SDK retries or automatic pagination; optional parameters use pointers. The client is safe for concurrent use when the injected HTTP client is safe for concurrent use.

Responses contain `Body`, `Status`, and `Headers`. Models and enum constants live in `github.com/envoapi-official/envoapi-sdks/go/api`. Nullable fields use `nullable.Nullable[T]`, distinguishing absent, null, and non-null values; union models provide typed `As...` helpers.

Use `errors.As` for `*envoapi.APIError`, `*envoapi.TransportError`, or `*envoapi.DecodeError`, and `errors.Is` for wrapped context cancellation and deadline errors. API errors include `Status`, `Code`, `Retryable`, `RequestID`, `Headers`, and raw `Body`.

## Local development and releases

To test local changes from another Go module:

```sh
go mod edit -require=github.com/envoapi-official/envoapi-sdks/go@v0.0.0
go mod edit -replace=github.com/envoapi-official/envoapi-sdks/go=/absolute/path/to/envoapi-sdks/go
go mod tidy
```

Release tags use the `go/` prefix, for example `go/v0.1.0`, because this module is in the repository's `go/` subdirectory. The repository must be public for unauthenticated installation through the public Go proxy. Go releases do not require a separate registry account or package upload.
