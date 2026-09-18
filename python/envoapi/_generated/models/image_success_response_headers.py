from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImageSuccessResponseHeaders")


@_attrs_define
class ImageSuccessResponseHeaders:
    """
    Attributes:
        date (str):
        cache_control (Literal['private, no-store']):
        vary (Literal['Accept']):
        x_request_id (str):
        content_type (Literal['image/jpeg']):
        content_length (int):
        content_disposition (Literal['inline']):
        accept_ranges (Literal['none']):
        x_content_type_options (Literal['nosniff']):
        cross_origin_resource_policy (Literal['cross-origin']):
    """

    date: str
    cache_control: Literal["private, no-store"]
    vary: Literal["Accept"]
    x_request_id: str
    content_type: Literal["image/jpeg"]
    content_length: int
    content_disposition: Literal["inline"]
    accept_ranges: Literal["none"]
    x_content_type_options: Literal["nosniff"]
    cross_origin_resource_policy: Literal["cross-origin"]

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        cache_control = self.cache_control

        vary = self.vary

        x_request_id = self.x_request_id

        content_type = self.content_type

        content_length = self.content_length

        content_disposition = self.content_disposition

        accept_ranges = self.accept_ranges

        x_content_type_options = self.x_content_type_options

        cross_origin_resource_policy = self.cross_origin_resource_policy

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Date": date,
                "Cache-Control": cache_control,
                "Vary": vary,
                "X-Request-Id": x_request_id,
                "Content-Type": content_type,
                "Content-Length": content_length,
                "Content-Disposition": content_disposition,
                "Accept-Ranges": accept_ranges,
                "X-Content-Type-Options": x_content_type_options,
                "Cross-Origin-Resource-Policy": cross_origin_resource_policy,
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

        vary = cast(Literal["Accept"], d.pop("Vary"))
        if vary != "Accept":
            raise ValueError(f"Vary must match const 'Accept', got '{vary}'")

        x_request_id = d.pop("X-Request-Id")
        if not isinstance(x_request_id, str):
            raise TypeError("Expected string for x_request_id")

        content_type = cast(Literal["image/jpeg"], d.pop("Content-Type"))
        if content_type != "image/jpeg":
            raise ValueError(f"Content-Type must match const 'image/jpeg', got '{content_type}'")

        content_length = d.pop("Content-Length")

        content_disposition = cast(Literal["inline"], d.pop("Content-Disposition"))
        if content_disposition != "inline":
            raise ValueError(f"Content-Disposition must match const 'inline', got '{content_disposition}'")

        accept_ranges = cast(Literal["none"], d.pop("Accept-Ranges"))
        if accept_ranges != "none":
            raise ValueError(f"Accept-Ranges must match const 'none', got '{accept_ranges}'")

        x_content_type_options = cast(Literal["nosniff"], d.pop("X-Content-Type-Options"))
        if x_content_type_options != "nosniff":
            raise ValueError(f"X-Content-Type-Options must match const 'nosniff', got '{x_content_type_options}'")

        cross_origin_resource_policy = cast(Literal["cross-origin"], d.pop("Cross-Origin-Resource-Policy"))
        if cross_origin_resource_policy != "cross-origin":
            raise ValueError(
                f"Cross-Origin-Resource-Policy must match const 'cross-origin', got '{cross_origin_resource_policy}'"
            )

        image_success_response_headers = cls(
            date=date,
            cache_control=cache_control,
            vary=vary,
            x_request_id=x_request_id,
            content_type=content_type,
            content_length=content_length,
            content_disposition=content_disposition,
            accept_ranges=accept_ranges,
            x_content_type_options=x_content_type_options,
            cross_origin_resource_policy=cross_origin_resource_policy,
        )

        return image_success_response_headers
