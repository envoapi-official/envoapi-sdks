from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="JobDetailsCompany")


@_attrs_define
class JobDetailsCompany:
    """
    Attributes:
        name (str):
        linkedin_url (str):
        logo_url (None | str):
        follower_count (int | None):
    """

    name: str
    linkedin_url: str
    logo_url: None | str
    follower_count: int | None

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        linkedin_url = self.linkedin_url

        logo_url: None | str
        logo_url = self.logo_url

        follower_count: int | None
        follower_count = self.follower_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "linkedinUrl": linkedin_url,
                "logoUrl": logo_url,
                "followerCount": follower_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        linkedin_url = d.pop("linkedinUrl")
        if not isinstance(linkedin_url, str):
            raise TypeError("Expected string for linkedin_url")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        def _parse_follower_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        follower_count = _parse_follower_count(d.pop("followerCount"))

        job_details_company = cls(
            name=name,
            linkedin_url=linkedin_url,
            logo_url=logo_url,
            follower_count=follower_count,
        )

        return job_details_company
