// Package envoapi provides typed clients for EnvoAPI's public API.
package envoapi

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"

	"github.com/envoapi-official/envoapi-sdks/go/api"
)

// Response preserves the API envelope and HTTP metadata.
type Response[T any] struct {
	Body    T
	Status  int
	Headers http.Header
}

type APIError struct {
	Status    int
	Code      string
	Message   string
	Retryable bool
	RequestID string
	Headers   http.Header
	Body      []byte
}

func (e *APIError) Error() string { return fmt.Sprintf("EnvoAPI HTTP %d: %s", e.Status, e.Message) }

type TransportError struct{ Err error }

func (e *TransportError) Error() string { return "EnvoAPI request failed: " + e.Err.Error() }
func (e *TransportError) Unwrap() error { return e.Err }

type DecodeError struct {
	Status  int
	Headers http.Header
	Err     error
}

func (e *DecodeError) Error() string { return "Invalid EnvoAPI response: " + e.Err.Error() }
func (e *DecodeError) Unwrap() error { return e.Err }

type Option func(*config)
type config struct {
	key, baseURL string
	timeout      time.Duration
	httpClient   api.HttpRequestDoer
}

func WithAPIKey(key string) Option      { return func(c *config) { c.key = key } }
func WithBaseURL(baseURL string) Option { return func(c *config) { c.baseURL = baseURL } }

// WithTimeout sets the whole-request timeout. The caller's earlier context deadline wins.
func WithTimeout(timeout time.Duration) Option { return func(c *config) { c.timeout = timeout } }

// WithHTTPClient replaces the transport. Callers control any retries made by this client.
func WithHTTPClient(client api.HttpRequestDoer) Option {
	return func(c *config) { c.httpClient = client }
}

// NewClient reads ENVOAPI_API_KEY unless WithAPIKey is supplied.
func NewClient(options ...Option) (*Client, error) {
	cfg := config{key: os.Getenv("ENVOAPI_API_KEY"), baseURL: "https://api.envoapi.com", timeout: 60 * time.Second}
	for _, option := range options {
		option(&cfg)
	}
	if strings.TrimSpace(cfg.key) == "" {
		return nil, errors.New("an EnvoAPI API key is required")
	}
	if cfg.timeout <= 0 {
		return nil, errors.New("timeout must be positive")
	}
	u, err := url.Parse(cfg.baseURL)
	if err != nil || u.Host == "" || (u.Scheme != "http" && u.Scheme != "https") || u.User != nil || u.RawQuery != "" || u.Fragment != "" {
		return nil, errors.New("invalid base URL")
	}
	if cfg.httpClient == nil {
		cfg.httpClient = &http.Client{CheckRedirect: func(r *http.Request, via []*http.Request) error { return http.ErrUseLastResponse }}
	}
	raw, err := api.NewClient(strings.TrimRight(cfg.baseURL, "/"), api.WithHTTPClient(cfg.httpClient), api.WithRequestEditorFn(func(ctx context.Context, r *http.Request) error {
		r.Header.Set("Authorization", "Bearer "+cfg.key)
		r.Header.Set("Accept", "application/json")
		r.Header.Set("User-Agent", "envoapi-go/0.1.1")
		return nil
	}))
	if err != nil {
		return nil, err
	}
	client := &Client{raw: raw, timeout: cfg.timeout}
	client.initResources()
	return client, nil
}

func decode[T any](response *http.Response, err error) (*Response[T], error) {
	if err != nil {
		return nil, &TransportError{Err: err}
	}
	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)
	if err != nil {
		return nil, &TransportError{Err: err}
	}
	if response.StatusCode < 200 || response.StatusCode >= 300 {
		envelope := struct {
			Error struct {
				Code      string
				Message   string
				Retryable bool
			}
			Meta struct{ RequestID string }
		}{}
		_ = json.Unmarshal(body, &envelope)
		id := envelope.Meta.RequestID
		if id == "" {
			id = response.Header.Get("X-Request-Id")
		}
		message := envelope.Error.Message
		if message == "" {
			message = http.StatusText(response.StatusCode)
		}
		return nil, &APIError{Status: response.StatusCode, Code: envelope.Error.Code, Message: message, Retryable: envelope.Error.Retryable, RequestID: id, Headers: response.Header.Clone(), Body: body}
	}
	var envelope map[string]json.RawMessage
	err = json.Unmarshal(body, &envelope)
	if err == nil {
		for _, key := range []string{"data", "meta"} {
			v := strings.TrimSpace(string(envelope[key]))
			if !strings.HasPrefix(v, "{") {
				err = errors.New("missing response envelope")
				break
			}
		}
	}
	var parsed T
	if err == nil {
		err = json.Unmarshal(body, &parsed)
	}
	if err != nil {
		return nil, &DecodeError{Status: response.StatusCode, Headers: response.Header.Clone(), Err: err}
	}
	return &Response[T]{Body: parsed, Status: response.StatusCode, Headers: response.Header.Clone()}, nil
}
