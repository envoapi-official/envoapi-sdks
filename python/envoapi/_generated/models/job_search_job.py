from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="JobSearchJob")


@_attrs_define
class JobSearchJob:
    """
    Attributes:
        title (str):
        url (str):
        location (None | str):
        posted_at (datetime.datetime | None):
        company_name (None | str):
        company_url (None | str):
        is_promoted (bool): Whether the job card is marked Promoted.
        is_easy_apply (bool): Whether the job card offers Easy Apply.
    """

    title: str
    url: str
    location: None | str
    posted_at: datetime.datetime | None
    company_name: None | str
    company_url: None | str
    is_promoted: bool
    is_easy_apply: bool

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

        company_name: None | str
        company_name = self.company_name

        company_url: None | str
        company_url = self.company_url

        is_promoted = self.is_promoted

        is_easy_apply = self.is_easy_apply

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "url": url,
                "location": location,
                "postedAt": posted_at,
                "companyName": company_name,
                "companyUrl": company_url,
                "isPromoted": is_promoted,
                "isEasyApply": is_easy_apply,
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

        def _parse_company_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_name = _parse_company_name(d.pop("companyName"))

        def _parse_company_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_url = _parse_company_url(d.pop("companyUrl"))

        is_promoted = d.pop("isPromoted")

        is_easy_apply = d.pop("isEasyApply")

        job_search_job = cls(
            title=title,
            url=url,
            location=location,
            posted_at=posted_at,
            company_name=company_name,
            company_url=company_url,
            is_promoted=is_promoted,
            is_easy_apply=is_easy_apply,
        )

        return job_search_job
