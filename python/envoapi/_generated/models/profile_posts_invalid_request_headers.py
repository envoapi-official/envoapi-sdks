from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilePostsInvalidRequestHeaders")


@_attrs_define
class ProfilePostsInvalidRequestHeaders:
    """
    Attributes:
        date (str):
        cache_control (Literal['private, no-store']):
        x_request_id (str):
        content_type (Literal['application/json; charset=utf-8']):
        x_rate_limit_limit (int | Unset):
        x_rate_limit_remaining (int | Unset):
        x_rate_limit_reset (int | Unset):
    """

    date: str
    cache_control: Literal["private, no-store"]
    x_request_id: str
    content_type: Literal["application/json; charset=utf-8"]
    x_rate_limit_limit: int | Unset = UNSET
    x_rate_limit_remaining: int | Unset = UNSET
    x_rate_limit_reset: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cache_control = self.cache_control

        x_request_id = self.x_request_id

        content_type = self.content_type

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
            }
        )
        if x_rate_limit_limit is not UNSET:
            field_dict["X-RateLimit-Limit"] = x_rate_limit_limit
        if x_rate_limit_remaining is not UNSET:
            field_dict["X-RateLimit-Remaining"] = x_rate_limit_remaining
        if x_rate_limit_reset is not UNSET:
            field_dict["X-RateLimit-Reset"] = x_rate_limit_reset

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

        x_rate_limit_limit = d.pop("X-RateLimit-Limit", UNSET)

        x_rate_limit_remaining = d.pop("X-RateLimit-Remaining", UNSET)

        x_rate_limit_reset = d.pop("X-RateLimit-Reset", UNSET)

        profile_posts_invalid_request_headers = cls(
            date=date,
            cache_control=cache_control,
            x_request_id=x_request_id,
            content_type=content_type,
            x_rate_limit_limit=x_rate_limit_limit,
            x_rate_limit_remaining=x_rate_limit_remaining,
            x_rate_limit_reset=x_rate_limit_reset,
        )

        return profile_posts_invalid_request_headers
