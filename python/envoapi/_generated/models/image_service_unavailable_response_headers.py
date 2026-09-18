from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageServiceUnavailableResponseHeaders")


@_attrs_define
class ImageServiceUnavailableResponseHeaders:
    """
    Attributes:
        date (str):
        cache_control (Literal['private, no-store']):
        vary (Literal['Accept']):
        x_request_id (str):
        content_type (Literal['application/json; charset=utf-8']):
        retry_after (int | Unset):
    """

    date: str
    cache_control: Literal["private, no-store"]
    vary: Literal["Accept"]
    x_request_id: str
    content_type: Literal["application/json; charset=utf-8"]
    retry_after: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cache_control = self.cache_control

        vary = self.vary

        x_request_id = self.x_request_id

        content_type = self.content_type

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Date": date,
                "Cache-Control": cache_control,
                "Vary": vary,
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

        vary = cast(Literal["Accept"], d.pop("Vary"))
        if vary != "Accept":
            raise ValueError(f"Vary must match const 'Accept', got '{vary}'")

        x_request_id = d.pop("X-Request-Id")
        if not isinstance(x_request_id, str):
            raise TypeError("Expected string for x_request_id")

        content_type = cast(Literal["application/json; charset=utf-8"], d.pop("Content-Type"))
        if content_type != "application/json; charset=utf-8":
            raise ValueError(f"Content-Type must match const 'application/json; charset=utf-8', got '{content_type}'")

        retry_after = d.pop("Retry-After", UNSET)

        image_service_unavailable_response_headers = cls(
            date=date,
            cache_control=cache_control,
            vary=vary,
            x_request_id=x_request_id,
            content_type=content_type,
            retry_after=retry_after,
        )

        return image_service_unavailable_response_headers
