from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_profile_detail_section import LinkedInV2ProfileDetailSection

T = TypeVar("T", bound="LinkedInV2ProfileDetailsQuery")


@_attrs_define
class LinkedInV2ProfileDetailsQuery:
    """
    Attributes:
        username (str):
        section (LinkedInV2ProfileDetailSection):
    """

    username: str
    section: LinkedInV2ProfileDetailSection

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        section = self.section.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "section": section,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        section = LinkedInV2ProfileDetailSection(d.pop("section"))

        linked_in_v2_profile_details_query = cls(
            username=username,
            section=section,
        )

        return linked_in_v2_profile_details_query
