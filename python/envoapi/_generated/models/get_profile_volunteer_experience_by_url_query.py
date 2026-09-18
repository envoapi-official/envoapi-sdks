from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetProfileVolunteerExperienceByUrlQuery")


@_attrs_define
class GetProfileVolunteerExperienceByUrlQuery:
    """
    Attributes:
        url (str):
    """

    url: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        get_profile_volunteer_experience_by_url_query = cls(
            url=url,
        )

        return get_profile_volunteer_experience_by_url_query
