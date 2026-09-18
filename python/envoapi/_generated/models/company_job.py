from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyJob")


@_attrs_define
class CompanyJob:
    """
    Attributes:
        title (str):
        url (str):
        location (None | str):
        posted_at (datetime.datetime | None):
    """

    title: str
    url: str
    location: None | str
    posted_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        location: None | str
        location = self.location

        posted_at: None | str
        if isinstance(self.posted_at, datetime.datetime):
            posted_at = self.posted_at.isoformat()
        else:
            posted_at = self.posted_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "url": url,
                "location": location,
                "postedAt": posted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")
        if not isinstance(title, str):
            raise TypeError("Expected string for title")

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_posted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                posted_at_type_0 = datetime.datetime.fromisoformat(data)

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        posted_at = _parse_posted_at(d.pop("postedAt"))

        company_job = cls(
            title=title,
            url=url,
            location=location,
            posted_at=posted_at,
        )

        return company_job
