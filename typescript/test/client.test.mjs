import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

// Breaking auth, routing, metadata, or error handling must fail at the HTTP boundary.
const sdk = await import("../dist/index.js").catch(() => ({}));
const posts = JSON.parse(
  readFileSync(new URL("../../tests/fixtures/posts.json", import.meta.url)),
);
const failure = JSON.parse(
  readFileSync(new URL("../../tests/fixtures/error.json", import.meta.url)),
);
const operations = JSON.parse(
  readFileSync(
    new URL("../../tests/fixtures/operations.json", import.meta.url),
  ),
);
const manifest = JSON.parse(
  readFileSync(new URL("../../openapi/operations.json", import.meta.url)),
);

for (const operation of manifest)
  test(`operation ${operation.operationId} routes and preserves its response`, async () => {
    const fixture = operations[operation.operationId];
    let calls = 0;
    const client = new sdk.EnvoAPI({
      apiKey: "key",
      fetch: async (request) => {
        calls++;
        const url = new URL(request.url);
        assert.equal(url.pathname, fixture.path);
        assert.deepEqual(
          Object.fromEntries(url.searchParams),
          Object.fromEntries(
            Object.entries(fixture.query).map(([k, v]) => [k, String(v)]),
          ),
        );
        return Response.json(fixture.response);
      },
    });
    const result = await client[operation.resource][operation.typescript](
      fixture.query,
    );
    assert.deepEqual(result.body, fixture.response);
    assert.equal(calls, 1);
  });

test("client exports exist", () =>
  assert.equal(typeof sdk.EnvoAPI, "function"));
test("missing credentials fail before any request", () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  const old = process.env.ENVOAPI_API_KEY;
  delete process.env.ENVOAPI_API_KEY;
  try {
    assert.throws(() => new sdk.EnvoAPI(), /API key/i);
  } finally {
    if (old !== undefined) process.env.ENVOAPI_API_KEY = old;
  }
});
test("posts preserve the envelope and cursor and make one authenticated request", async () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  let calls = 0;
  const client = new sdk.EnvoAPI({
    apiKey: "test-key",
    baseUrl: "https://sdk.test",
    fetch: async (request) => {
      calls++;
      assert.equal(request.headers.get("authorization"), "Bearer test-key");
      assert.equal(
        request.url,
        "https://sdk.test/v1/profiles/posts?username=alice&cursor=cursor_Previous123",
      );
      return Response.json(posts, {
        headers: { "x-request-id": "req_sdk_test" },
      });
    },
  });
  const result = await client.profiles.getPosts({
    username: "alice",
    cursor: "cursor_Previous123",
  });
  assert.deepEqual(result.body, posts);
  assert.equal(result.headers.get("x-request-id"), "req_sdk_test");
  assert.equal(result.status, 200);
  assert.equal(calls, 1);
});
for (const [status, code, retryable] of [
  [400, "invalid_request", false],
  [401, "invalid_api_key", false],
  [404, "resource_not_found", false],
  [429, "rate_limit_exceeded", true],
  [503, "service_unavailable", true],
]) {
  test(`HTTP ${status} yields a structured error without retry`, async () => {
    assert.equal(typeof sdk.EnvoAPI, "function");
    let calls = 0;
    const client = new sdk.EnvoAPI({
      apiKey: "key",
      fetch: async () => {
        calls++;
        return Response.json(
          { ...failure, error: { ...failure.error, code, retryable } },
          { status, headers: { "retry-after": "5" } },
        );
      },
    });
    await assert.rejects(
      client.profiles.getPosts({ username: "alice" }),
      (e) => {
        assert.ok(e instanceof sdk.APIError);
        assert.equal(e.status, status);
        assert.equal(e.code, code);
        assert.equal(e.retryable, retryable);
        assert.equal(e.requestId, "req_sdk_test");
        assert.equal(e.headers.get("retry-after"), "5");
        return true;
      },
    );
    assert.equal(calls, 1);
  });
}
test("non-JSON HTTP errors retain status and headers", async () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  const client = new sdk.EnvoAPI({
    apiKey: "key",
    fetch: async () =>
      new Response("gateway unavailable", {
        status: 502,
        headers: { "x-request-id": "req_proxy" },
      }),
  });
  await assert.rejects(
    client.profiles.getPosts({ username: "alice" }),
    (e) =>
      e instanceof sdk.APIError &&
      e.status === 502 &&
      e.requestId === "req_proxy",
  );
});
test("malformed successful responses are decoding errors", async () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  for (const value of ["{", "null", "{}"]) {
    const client = new sdk.EnvoAPI({
      apiKey: "key",
      fetch: async () =>
        new Response(value, {
          headers: { "content-type": "application/json" },
        }),
    });
    await assert.rejects(
      client.profiles.getPosts({ username: "alice" }),
      sdk.DecodeError,
    );
  }
});
test("transport failures retain their cause", async () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  const cause = new Error("connection reset");
  const client = new sdk.EnvoAPI({
    apiKey: "key",
    fetch: async () => {
      throw cause;
    },
  });
  await assert.rejects(
    client.profiles.getPosts({ username: "alice" }),
    (e) => e instanceof sdk.TransportError && e.cause === cause,
  );
});
test("cancellation reaches the transport", async () => {
  assert.equal(typeof sdk.EnvoAPI, "function");
  const controller = new AbortController();
  controller.abort();
  const client = new sdk.EnvoAPI({
    apiKey: "key",
    fetch: async (request) => {
      request.signal.throwIfAborted();
      return Response.json(posts);
    },
  });
  await assert.rejects(
    client.profiles.getPosts(
      { username: "alice" },
      { signal: controller.signal },
    ),
    sdk.TransportError,
  );
});

test("deadline aborts a pending request without retry", async () => {
  let calls = 0;
  const client = new sdk.EnvoAPI({
    apiKey: "key",
    timeoutMs: 5,
    fetch: (request) => {
      calls++;
      return new Promise((resolve, reject) => {
        request.signal.addEventListener(
          "abort",
          () => reject(request.signal.reason),
          { once: true },
        );
      });
    },
  });
  await assert.rejects(
    client.profiles.getPosts({ username: "alice" }),
    sdk.TransportError,
  );
  assert.equal(calls, 1);
});

test("nullable company-reference union branches survive the response", async () => {
  const companyInterests = [
    { publicId: "company_123", name: null },
    { publicId: null, name: "Sample company" },
    { publicId: "company_123", name: "Sample company" },
  ];
  const body = { data: { companyInterests }, meta: { creditCost: 1 } };
  const client = new sdk.EnvoAPI({
    apiKey: "key",
    fetch: async () => Response.json(body),
  });
  assert.deepEqual(
    (await client.profiles.getCompanyInterestsByUsername({ username: "alice" }))
      .body,
    body,
  );
});
