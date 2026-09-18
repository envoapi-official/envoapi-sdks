from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImageVariant")


@_attrs_define
class ImageVariant:
    """
    Attributes:
        url (str):
        width (int | None):
        height (int | None):
    """

    url: str
    width: int | None
    height: int | None

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        width: int | None
        width = self.width

        height: int | None
        height = self.height

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "width": width,
                "height": height,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_width(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        width = _parse_width(d.pop("width"))

        def _parse_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        height = _parse_height(d.pop("height"))

        image_variant = cls(
            url=url,
            width=width,
            height=height,
        )

        return image_variant
