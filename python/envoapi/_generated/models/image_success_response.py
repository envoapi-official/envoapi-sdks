from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import File

if TYPE_CHECKING:
    from ..models.image_success_response_headers import ImageSuccessResponseHeaders


T = TypeVar("T", bound="ImageSuccessResponse")


@_attrs_define
class ImageSuccessResponse:
    """
    Attributes:
        body (File):
        headers (ImageSuccessResponseHeaders):
    """

    body: File
    headers: ImageSuccessResponseHeaders

    def to_dict(self) -> dict[str, Any]:
        body = self.body.to_tuple()

        headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body": body,
                "headers": headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_success_response_headers import ImageSuccessResponseHeaders  # noqa: PLC0415

        d = dict(src_dict)
        body = File(payload=BytesIO(d.pop("body")))

        headers = ImageSuccessResponseHeaders.from_dict(d.pop("headers"))

        image_success_response = cls(
            body=body,
            headers=headers,
        )

        return image_success_response
