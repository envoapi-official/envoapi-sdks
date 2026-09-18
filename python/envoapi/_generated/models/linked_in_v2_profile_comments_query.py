from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2ProfileCommentsQuery")


@_attrs_define
class LinkedInV2ProfileCommentsQuery:
    """
    Attributes:
        username (str):
        cursor (str | Unset): Opaque Envo continuation cursor. Reuse with the same account and username; use it before
            expiry. The backend fixes the page size.
    """

    username: str
    cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        cursor = self.cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        cursor = d.pop("cursor", UNSET)

        linked_in_v2_profile_comments_query = cls(
            username=username,
            cursor=cursor,
        )

        return linked_in_v2_profile_comments_query
