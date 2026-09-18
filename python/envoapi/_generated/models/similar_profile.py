from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimilarProfile")


@_attrs_define
class SimilarProfile:
    """
    Attributes:
        username (str):
        profile_url (str):
        full_name (str):
        headline (str):
        profile_picture_url (None | str):
    """

    username: str
    profile_url: str
    full_name: str
    headline: str
    profile_picture_url: None | str

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        profile_url = self.profile_url

        full_name = self.full_name

        headline = self.headline

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "profileUrl": profile_url,
                "fullName": full_name,
                "headline": headline,
                "profilePictureUrl": profile_picture_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        profile_url = d.pop("profileUrl")
        if not isinstance(profile_url, str):
            raise TypeError("Expected string for profile_url")

        full_name = d.pop("fullName")
        if not isinstance(full_name, str):
            raise TypeError("Expected string for full_name")

        headline = d.pop("headline")
        if not isinstance(headline, str):
            raise TypeError("Expected string for headline")

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profilePictureUrl"))

        similar_profile = cls(
            username=username,
            profile_url=profile_url,
            full_name=full_name,
            headline=headline,
            profile_picture_url=profile_picture_url,
        )

        return similar_profile
