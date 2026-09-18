package envoapi

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"net/http/httptest"
	"os"
	"reflect"
	"strings"
	"testing"
	"time"

	"github.com/envoapi/sdks/go/api"
)

func TestNullableUnionBranches(t *testing.T) {
	for _, body := range []string{`{"publicId":"company_123","name":null}`, `{"publicId":null,"name":"Sample company"}`, `{"publicId":"company_123","name":"Sample company"}`} {
		var model api.CompanyReference
		if err := json.Unmarshal([]byte(body), &model); err != nil {
			t.Fatal(err)
		}
		encoded, err := json.Marshal(model)
		if err != nil {
			t.Fatal(err)
		}
		var got, want any
		json.Unmarshal(encoded, &got)
		json.Unmarshal([]byte(body), &want)
		if !reflect.DeepEqual(got, want) {
			t.Fatal("union lost fields", string(encoded))
		}
	}
	var model api.CompanyReference
	json.Unmarshal([]byte(`{"publicId":null,"name":"Sample company"}`), &model)
	typed, err := model.AsCompanyReference1()
	if err != nil || !typed.PublicId.IsNull() || typed.Name != "Sample company" {
		t.Fatal("typed nullable branch lost", typed, err)
	}
}

func TestAllOperations(t *testing.T) {
	var cases map[string]struct {
		Path     string
		Query    map[string]any
		Response json.RawMessage
	}
	if err := json.Unmarshal(fixture(t, "operations"), &cases); err != nil {
		t.Fatal(err)
	}
	manifestBytes, err := os.ReadFile("../openapi/operations.json")
	if err != nil {
		t.Fatal(err)
	}
	var manifest []struct {
		OperationID string
		Resource    string
		Go          string
	}
	if err := json.Unmarshal(manifestBytes, &manifest); err != nil {
		t.Fatal(err)
	}
	for _, operation := range manifest {
		t.Run(operation.OperationID, func(t *testing.T) {
			entry := cases[operation.OperationID]
			calls := 0
			server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				calls++
				if r.URL.Path != entry.Path {
					t.Error("incorrect path", r.URL.Path)
				}
				if len(r.URL.Query()) != len(entry.Query) {
					t.Error("unexpected parameters", r.URL.Query())
				}
				for k, v := range entry.Query {
					if r.URL.Query().Get(k) != fmt.Sprint(v) {
						t.Error("wrong parameter", k)
					}
				}
				w.Header().Set("Content-Type", "application/json")
				w.Write(entry.Response)
			}))
			defer server.Close()
			client, _ := NewClient(WithAPIKey("key"), WithBaseURL(server.URL))
			resource := reflect.ValueOf(client).Elem().FieldByName(strings.ToUpper(operation.Resource[:1]) + operation.Resource[1:])
			method := resource.MethodByName(operation.Go)
			if !method.IsValid() {
				t.Fatal("missing resource method")
			}
			params := reflect.New(method.Type().In(1))
			query, _ := json.Marshal(entry.Query)
			if err := json.Unmarshal(query, params.Interface()); err != nil {
				t.Fatal(err)
			}
			result := method.Call([]reflect.Value{reflect.ValueOf(context.Background()), params.Elem()})
			if !result[1].IsNil() {
				t.Fatal(result[1].Interface())
			}
			body := result[0].Elem().FieldByName("Body").Interface()
			actual, err := json.Marshal(body)
			if err != nil {
				t.Fatal(err)
			}
			var got, want any
			json.Unmarshal(actual, &got)
			json.Unmarshal(entry.Response, &want)
			if !reflect.DeepEqual(got, want) {
				t.Fatalf("roundtrip mismatch\ngot %s\nwant %s", actual, entry.Response)
			}
			if calls != 1 {
				t.Fatal("extra requests", calls)
			}
		})
	}
}

func fixture(t *testing.T, name string) []byte {
	t.Helper()
	b, e := os.ReadFile("../tests/fixtures/" + name + ".json")
	if e != nil {
		t.Fatal(e)
	}
	return b
}

func TestMissingCredentials(t *testing.T) {
	t.Setenv("ENVOAPI_API_KEY", "")
	if _, err := NewClient(); err == nil {
		t.Fatal("expected missing API key error")
	}
}

func TestPostsEnvelopeAndSingleRequest(t *testing.T) {
	body := fixture(t, "posts")
	calls := 0
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		calls++
		if r.Header.Get("Authorization") != "Bearer key" {
			t.Error("missing authentication")
		}
		if r.URL.Path != "/v1/profiles/posts" || r.URL.Query().Get("username") != "alice" || r.URL.Query().Get("cursor") != "cursor_Previous123" {
			t.Error("wrong query", r.URL)
		}
		w.Header().Set("X-Request-Id", "req_sdk_test")
		w.Header().Set("Content-Type", "application/json")
		w.Write(body)
	}))
	defer server.Close()
	client, err := NewClient(WithAPIKey("key"), WithBaseURL(server.URL))
	if err != nil {
		t.Fatal(err)
	}
	cursor := "cursor_Previous123"
	result, err := client.Profiles.GetPosts(context.Background(), GetProfilePostsParams{Username: "alice", Cursor: &cursor})
	if err != nil {
		t.Fatal(err)
	}
	if result.Body.Meta.CreditCost != 1 || result.Status != 200 || result.Headers.Get("X-Request-Id") != "req_sdk_test" || calls != 1 {
		t.Fatal("lost metadata or extra requests", result, calls)
	}
	b, err := json.Marshal(result.Body)
	if err != nil {
		t.Fatal(err)
	}
	var got, want any
	json.Unmarshal(b, &got)
	json.Unmarshal(body, &want)
	gb, _ := json.Marshal(got)
	wb, _ := json.Marshal(want)
	if string(gb) != string(wb) {
		t.Fatalf("roundtrip mismatch: %s", b)
	}
}

func TestAPIErrorsDoNotRetry(t *testing.T) {
	for _, status := range []int{400, 401, 404, 429, 503} {
		t.Run(http.StatusText(status), func(t *testing.T) {
			calls := 0
			server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
				calls++
				w.Header().Set("Retry-After", "5")
				w.WriteHeader(status)
				w.Write(fixture(t, "error"))
			}))
			defer server.Close()
			client, _ := NewClient(WithAPIKey("key"), WithBaseURL(server.URL))
			_, err := client.Profiles.GetPosts(context.Background(), GetProfilePostsParams{Username: "alice"})
			var e *APIError
			if !errors.As(err, &e) {
				t.Fatalf("expected APIError, got %v", err)
			}
			if e.Status != status || e.Code != "rate_limit_exceeded" || !e.Retryable || e.RequestID != "req_sdk_test" || e.Headers.Get("Retry-After") != "5" || calls != 1 {
				t.Fatal("lost error details", e, calls)
			}
		})
	}
}

func TestMalformedResponses(t *testing.T) {
	for _, body := range []string{"{", "null", "{}"} {
		t.Run(body, func(t *testing.T) {
			server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { w.Write([]byte(body)) }))
			defer server.Close()
			client, _ := NewClient(WithAPIKey("key"), WithBaseURL(server.URL))
			_, err := client.Profiles.GetPosts(context.Background(), GetProfilePostsParams{Username: "alice"})
			var e *DecodeError
			if !errors.As(err, &e) {
				t.Fatalf("expected DecodeError, got %v", err)
			}
		})
	}
}

func TestNonJSONError(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("X-Request-Id", "req_proxy")
		w.WriteHeader(502)
		w.Write([]byte("bad gateway"))
	}))
	defer server.Close()
	client, _ := NewClient(WithAPIKey("key"), WithBaseURL(server.URL))
	_, err := client.Profiles.GetPosts(context.Background(), GetProfilePostsParams{Username: "alice"})
	var e *APIError
	if !errors.As(err, &e) || e.Status != 502 || e.RequestID != "req_proxy" {
		t.Fatal(err)
	}
}

func TestCancellationAndTimeout(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { <-r.Context().Done() }))
	defer server.Close()
	client, _ := NewClient(WithAPIKey("key"), WithBaseURL(server.URL), WithTimeout(10*time.Millisecond))
	_, err := client.Profiles.GetPosts(context.Background(), GetProfilePostsParams{Username: "alice"})
	var e *TransportError
	if !errors.As(err, &e) || !errors.Is(err, context.DeadlineExceeded) {
		t.Fatalf("expected timeout, got %v", err)
	}
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	_, err = client.Profiles.GetPosts(ctx, GetProfilePostsParams{Username: "alice"})
	if !errors.Is(err, context.Canceled) {
		t.Fatalf("expected cancellation, got %v", err)
	}
}
