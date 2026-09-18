from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileLookupQueryType1")


@_attrs_define
class ProfileLookupQueryType1:
    """
    Attributes:
        username (str):
    """

    username: str

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        profile_lookup_query_type_1 = cls(
            username=username,
        )

        return profile_lookup_query_type_1
