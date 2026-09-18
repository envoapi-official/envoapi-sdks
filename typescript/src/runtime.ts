import createClient from "openapi-fetch";
import type { paths } from "./schema.js";

export interface ClientOptions {
  apiKey?: string;
  baseUrl?: string;
  /** Whole-request timeout, including reading the response body. Defaults to 60 seconds. */
  timeoutMs?: number;
  fetch?: typeof globalThis.fetch;
}
export interface RequestOptions {
  signal?: AbortSignal;
}
export interface APIResponse<T> {
  body: T;
  status: number;
  headers: Headers;
}

export class APIError extends Error {
  readonly code?: string;
  readonly retryable: boolean;
  readonly requestId?: string;
  constructor(
    readonly status: number,
    readonly headers: Headers,
    readonly body: unknown,
  ) {
    const envelope = isObject(body) ? body : {};
    const error = isObject(envelope.error) ? envelope.error : {};
    const meta = isObject(envelope.meta) ? envelope.meta : {};
    super(typeof error.message === "string" ? error.message : `HTTP ${status}`);
    this.name = "APIError";
    this.code = typeof error.code === "string" ? error.code : undefined;
    this.retryable = error.retryable === true;
    this.requestId =
      typeof meta.requestId === "string"
        ? meta.requestId
        : (headers.get("x-request-id") ?? undefined);
  }
}
export class TransportError extends Error {
  constructor(cause: unknown) {
    super("EnvoAPI request failed", { cause });
    this.name = "TransportError";
  }
}
export class DecodeError extends Error {
  constructor(
    readonly status: number,
    readonly headers: Headers,
    cause?: unknown,
  ) {
    super("Invalid EnvoAPI response", { cause });
    this.name = "DecodeError";
  }
}
const isObject = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === "object" && !Array.isArray(value);

export class Transport {
  private readonly client;
  private readonly timeoutMs: number;
  constructor(options: ClientOptions) {
    const env = (
      globalThis as { process?: { env?: Record<string, string | undefined> } }
    ).process?.env;
    const key = options.apiKey ?? env?.ENVOAPI_API_KEY;
    if (!key?.trim()) throw new Error("An EnvoAPI API key is required");
    this.timeoutMs = options.timeoutMs ?? 60_000;
    if (!Number.isFinite(this.timeoutMs) || this.timeoutMs <= 0)
      throw new Error("timeoutMs must be positive");
    const baseUrl = options.baseUrl ?? "https://api.envoapi.com";
    const url = new URL(baseUrl);
    if (
      !["http:", "https:"].includes(url.protocol) ||
      url.username ||
      url.password ||
      url.search ||
      url.hash
    )
      throw new Error("Invalid base URL");
    this.client = createClient<paths>({
      baseUrl: baseUrl.replace(/\/$/, ""),
      fetch: options.fetch,
      headers: {
        Authorization: `Bearer ${key}`,
        Accept: "application/json",
        "User-Agent": "envoapi-typescript/0.1.3",
      },
      redirect: "error",
    });
  }
  async request<T>(
    path: keyof paths,
    query: Record<string, unknown> | undefined,
    options: RequestOptions = {},
  ): Promise<APIResponse<T>> {
    const controller = new AbortController();
    const timer = setTimeout(
      () => controller.abort(new Error("EnvoAPI request timed out")),
      this.timeoutMs,
    );
    const signal = options.signal
      ? AbortSignal.any([controller.signal, options.signal])
      : controller.signal;
    try {
      let response: Response, text: string;
      try {
        // Resource methods supply the path-specific query type. Parsing text here preserves non-JSON HTTP errors.
        const result = await this.client.GET(path, {
          params: { query } as never,
          signal,
          parseAs: "text",
        });
        response = result.response;
        text = (result.data ?? result.error ?? "") as string;
        if (typeof text !== "string") text = JSON.stringify(text);
      } catch (cause) {
        throw new TransportError(cause);
      }
      let body: unknown;
      try {
        body = JSON.parse(text);
      } catch (cause) {
        if (!response.ok)
          throw new APIError(response.status, response.headers, text);
        throw new DecodeError(response.status, response.headers, cause);
      }
      if (!response.ok)
        throw new APIError(response.status, response.headers, body);
      if (!isObject(body) || !isObject(body.data) || !isObject(body.meta))
        throw new DecodeError(response.status, response.headers);
      return {
        body: body as T,
        status: response.status,
        headers: response.headers,
      };
    } finally {
      clearTimeout(timer);
    }
  }
}
