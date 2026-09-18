from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="LookupAdmittedErrorResponseHeaders")


@_attrs_define
class LookupAdmittedErrorResponseHeaders:
    """
    Attributes:
        date (str):
        cache_control (Literal['private, no-store']):
        x_request_id (str):
        content_type (Literal['application/json; charset=utf-8']):
        x_credits_remaining (int):
        x_rate_limit_limit (int):
        x_rate_limit_remaining (int):
        x_rate_limit_reset (int):
    """

    date: str
    cache_control: Literal["private, no-store"]
    x_request_id: str
    content_type: Literal["application/json; charset=utf-8"]
    x_credits_remaining: int
    x_rate_limit_limit: int
    x_rate_limit_remaining: int
    x_rate_limit_reset: int

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cache_control = self.cache_control

        x_request_id = self.x_request_id

        content_type = self.content_type

        x_credits_remaining = self.x_credits_remaining

        x_rate_limit_limit = self.x_rate_limit_limit

        x_rate_limit_remaining = self.x_rate_limit_remaining

        x_rate_limit_reset = self.x_rate_limit_reset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Date": date,
                "Cache-Control": cache_control,
                "X-Request-Id": x_request_id,
                "Content-Type": content_type,
                "X-Credits-Remaining": x_credits_remaining,
                "X-RateLimit-Limit": x_rate_limit_limit,
                "X-RateLimit-Remaining": x_rate_limit_remaining,
                "X-RateLimit-Reset": x_rate_limit_reset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("Date")
        if not isinstance(date, str):
            raise TypeError("Expected string for date")

        cache_control = cast(Literal["private, no-store"], d.pop("Cache-Control"))
        if cache_control != "private, no-store":
            raise ValueError(f"Cache-Control must match const 'private, no-store', got '{cache_control}'")

        x_request_id = d.pop("X-Request-Id")
        if not isinstance(x_request_id, str):
            raise TypeError("Expected string for x_request_id")

        content_type = cast(Literal["application/json; charset=utf-8"], d.pop("Content-Type"))
        if content_type != "application/json; charset=utf-8":
            raise ValueError(f"Content-Type must match const 'application/json; charset=utf-8', got '{content_type}'")

        x_credits_remaining = d.pop("X-Credits-Remaining")

        x_rate_limit_limit = d.pop("X-RateLimit-Limit")

        x_rate_limit_remaining = d.pop("X-RateLimit-Remaining")

        x_rate_limit_reset = d.pop("X-RateLimit-Reset")

        lookup_admitted_error_response_headers = cls(
            date=date,
            cache_control=cache_control,
            x_request_id=x_request_id,
            content_type=content_type,
            x_credits_remaining=x_credits_remaining,
            x_rate_limit_limit=x_rate_limit_limit,
            x_rate_limit_remaining=x_rate_limit_remaining,
            x_rate_limit_reset=x_rate_limit_reset,
        )

        return lookup_admitted_error_response_headers
