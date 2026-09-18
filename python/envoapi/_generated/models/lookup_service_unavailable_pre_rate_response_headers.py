from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookupServiceUnavailablePreRateResponseHeaders")


@_attrs_define
class LookupServiceUnavailablePreRateResponseHeaders:
    """
    Attributes:
        date (str):
        cache_control (Literal['private, no-store']):
        x_request_id (str):
        content_type (Literal['application/json; charset=utf-8']):
        retry_after (int | Unset):
    """

    date: str
    cache_control: Literal["private, no-store"]
    x_request_id: str
    content_type: Literal["application/json; charset=utf-8"]
    retry_after: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cache_control = self.cache_control

        x_request_id = self.x_request_id

        content_type = self.content_type

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Date": date,
                "Cache-Control": cache_control,
                "X-Request-Id": x_request_id,
                "Content-Type": content_type,
            }
        )
        if retry_after is not UNSET:
            field_dict["Retry-After"] = retry_after

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

        retry_after = d.pop("Retry-After", UNSET)

        lookup_service_unavailable_pre_rate_response_headers = cls(
            date=date,
            cache_control=cache_control,
            x_request_id=x_request_id,
            content_type=content_type,
            retry_after=retry_after,
        )

        return lookup_service_unavailable_pre_rate_response_headers
