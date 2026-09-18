from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_profile_section_query_section import LinkedInV2ProfileSectionQuerySection

T = TypeVar("T", bound="LinkedInV2ProfileSectionQuery")


@_attrs_define
class LinkedInV2ProfileSectionQuery:
    """
    Attributes:
        username (str):
        section (LinkedInV2ProfileSectionQuerySection):
    """

    username: str
    section: LinkedInV2ProfileSectionQuerySection

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

        section = LinkedInV2ProfileSectionQuerySection(d.pop("section"))

        linked_in_v2_profile_section_query = cls(
            username=username,
            section=section,
        )

        return linked_in_v2_profile_section_query
