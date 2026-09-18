from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyPerson")


@_attrs_define
class CompanyPerson:
    """
    Attributes:
        id (None | str):
        headline (None | str):
        profile_picture_url (None | str):
    """

    id: None | str
    headline: None | str
    profile_picture_url: None | str

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        headline: None | str
        headline = self.headline

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "headline": headline,
                "profilePictureUrl": profile_picture_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profilePictureUrl"))

        company_person = cls(
            id=id,
            headline=headline,
            profile_picture_url=profile_picture_url,
        )

        return company_person
