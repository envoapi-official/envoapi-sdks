from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetProfileCompanyInterestsByUrlQuery")


@_attrs_define
class GetProfileCompanyInterestsByUrlQuery:
    """
    Attributes:
        url (str):
        start (int):  Default: 0.
    """

    url: str
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        start = d.pop("start")

        get_profile_company_interests_by_url_query = cls(
            url=url,
            start=start,
        )

        return get_profile_company_interests_by_url_query
