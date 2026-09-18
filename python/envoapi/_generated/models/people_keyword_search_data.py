from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_profile import PeopleKeywordSearchProfile


T = TypeVar("T", bound="PeopleKeywordSearchData")


@_attrs_define
class PeopleKeywordSearchData:
    """
    Attributes:
        profiles (list[PeopleKeywordSearchProfile]):
    """

    profiles: list[PeopleKeywordSearchProfile]

    def to_dict(self) -> dict[str, Any]:
        profiles = []
        for profiles_item_data in self.profiles:
            profiles_item = profiles_item_data.to_dict()
            profiles.append(profiles_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "profiles": profiles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_keyword_search_profile import PeopleKeywordSearchProfile  # noqa: PLC0415

        d = dict(src_dict)
        profiles = []
        _profiles = d.pop("profiles")
        for profiles_item_data in _profiles:
            profiles_item = PeopleKeywordSearchProfile.from_dict(profiles_item_data)

            profiles.append(profiles_item)

        people_keyword_search_data = cls(
            profiles=profiles,
        )

        return people_keyword_search_data
