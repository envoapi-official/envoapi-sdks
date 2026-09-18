"""Shared transport policy for the synchronous and asynchronous clients."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

import httpx

T = TypeVar("T")


@dataclass(frozen=True)
class Response(Generic[T]):
    body: T
    status: int
    headers: httpx.Headers


class APIError(Exception):
    def __init__(self, status: int, headers: httpx.Headers, body: Any):
        envelope = body if isinstance(body, dict) else {}
        error = envelope.get("error", {})
        error = error if isinstance(error, dict) else {}
        meta = envelope.get("meta", {})
        meta = meta if isinstance(meta, dict) else {}
        super().__init__(error.get("message") or f"HTTP {status}")
        self.status = status
        self.headers = headers
        self.body = body
        self.code = error.get("code")
        self.retryable = error.get("retryable") is True
        self.request_id = meta.get("requestId") or headers.get("x-request-id")


class TransportError(Exception):
    """A transport failure; the original HTTPX exception is __cause__."""


class DecodeError(Exception):
    def __init__(self, status: int, headers: httpx.Headers):
        super().__init__("Invalid EnvoAPI response")
        self.status = status
        self.headers = headers


def _options(api_key: str | None, base_url: str, timeout: float | httpx.Timeout) -> dict[str, Any]:
    key = api_key if api_key is not None else os.environ.get("ENVOAPI_API_KEY")
    if not key or not key.strip():
        raise ValueError("An EnvoAPI API key is required")
    url = httpx.URL(base_url)
    if url.scheme not in ("http", "https") or not url.host or url.userinfo or url.query or url.fragment:
        raise ValueError("Invalid base URL")
    if isinstance(timeout, (int, float)) and timeout <= 0:
        raise ValueError("timeout must be positive")
    return dict(
        base_url=base_url.rstrip("/"),
        timeout=timeout,
        follow_redirects=False,
        headers={"Authorization": f"Bearer {key}", "Accept": "application/json", "User-Agent": "envoapi-python/0.1.0"},
    )


def _decode(response: httpx.Response, model: type[T]) -> Response[T]:
    try:
        body = response.json()
    except ValueError as exc:
        if not response.is_success:
            raise APIError(response.status_code, response.headers, response.text) from exc
        raise DecodeError(response.status_code, response.headers) from exc
    if not response.is_success:
        raise APIError(response.status_code, response.headers, body)
    try:
        if (
            not isinstance(body, dict)
            or not isinstance(body.get("data"), dict)
            or not isinstance(body.get("meta"), dict)
        ):
            raise ValueError("Missing response envelope")
        parsed = model.from_dict(body)  # type: ignore[attr-defined]
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        raise DecodeError(response.status_code, response.headers) from exc
    return Response(parsed, response.status_code, response.headers)


class SyncTransport:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = "https://api.envoapi.com",
        timeout: float | httpx.Timeout = 60.0,
        transport: httpx.BaseTransport | None = None,
    ):
        self._http = httpx.Client(**_options(api_key, base_url, timeout), transport=transport)

    def _request(self, model: type[T], kwargs: dict[str, Any]) -> Response[T]:
        try:
            response = self._http.request(**kwargs)
        except httpx.RequestError as exc:
            raise TransportError("EnvoAPI request failed") from exc
        return _decode(response, model)

    def close(self) -> None:
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncTransport:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = "https://api.envoapi.com",
        timeout: float | httpx.Timeout = 60.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ):
        self._http = httpx.AsyncClient(**_options(api_key, base_url, timeout), transport=transport)

    async def _request(self, model: type[T], kwargs: dict[str, Any]) -> Response[T]:
        try:
            response = await self._http.request(**kwargs)
        except httpx.RequestError as exc:
            raise TransportError("EnvoAPI request failed") from exc
        return _decode(response, model)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.aclose()
