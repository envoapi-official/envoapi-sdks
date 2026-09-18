from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.social_handle_platform import SocialHandlePlatform

T = TypeVar("T", bound="SocialHandle")


@_attrs_define
class SocialHandle:
    """
    Attributes:
        platform (SocialHandlePlatform):
        handle (str):
    """

    platform: SocialHandlePlatform
    handle: str

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        handle = self.handle

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "platform": platform,
                "handle": handle,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = SocialHandlePlatform(d.pop("platform"))

        handle = d.pop("handle")
        if not isinstance(handle, str):
            raise TypeError("Expected string for handle")

        social_handle = cls(
            platform=platform,
            handle=handle,
        )

        return social_handle
