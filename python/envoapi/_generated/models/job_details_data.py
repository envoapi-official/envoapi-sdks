from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.job_details_data_status import JobDetailsDataStatus

if TYPE_CHECKING:
    from ..models.job_details_company import JobDetailsCompany


T = TypeVar("T", bound="JobDetailsData")


@_attrs_define
class JobDetailsData:
    """
    Attributes:
        url (str):
        title (str):
        description (str):
        company (JobDetailsCompany):
        location (str):
        workplace_type (None | str):
        employment_type (None | str):
        posted_at (datetime.datetime):
        posted_on_text (str):
        status (JobDetailsDataStatus):
        is_reposted (bool):
    """

    url: str
    title: str
    description: str
    company: JobDetailsCompany
    location: str
    workplace_type: None | str
    employment_type: None | str
    posted_at: datetime.datetime
    posted_on_text: str
    status: JobDetailsDataStatus
    is_reposted: bool

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        title = self.title

        description = self.description

        company = self.company.to_dict()

        location = self.location

        workplace_type: None | str
        workplace_type = self.workplace_type

        employment_type: None | str
        employment_type = self.employment_type

        posted_at = self.posted_at.isoformat()

        posted_on_text = self.posted_on_text

        status = self.status.value

        is_reposted = self.is_reposted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "title": title,
                "description": description,
                "company": company,
                "location": location,
                "workplaceType": workplace_type,
                "employmentType": employment_type,
                "postedAt": posted_at,
                "postedOnText": posted_on_text,
                "status": status,
                "isReposted": is_reposted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_details_company import JobDetailsCompany  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        title = d.pop("title")
        if not isinstance(title, str):
            raise TypeError("Expected string for title")

        description = d.pop("description")
        if not isinstance(description, str):
            raise TypeError("Expected string for description")

        company = JobDetailsCompany.from_dict(d.pop("company"))

        location = d.pop("location")
        if not isinstance(location, str):
            raise TypeError("Expected string for location")

        def _parse_workplace_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workplace_type = _parse_workplace_type(d.pop("workplaceType"))

        def _parse_employment_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        employment_type = _parse_employment_type(d.pop("employmentType"))

        posted_at = datetime.datetime.fromisoformat(d.pop("postedAt"))

        posted_on_text = d.pop("postedOnText")
        if not isinstance(posted_on_text, str):
            raise TypeError("Expected string for posted_on_text")

        status = JobDetailsDataStatus(d.pop("status"))

        is_reposted = d.pop("isReposted")

        job_details_data = cls(
            url=url,
            title=title,
            description=description,
            company=company,
            location=location,
            workplace_type=workplace_type,
            employment_type=employment_type,
            posted_at=posted_at,
            posted_on_text=posted_on_text,
            status=status,
            is_reposted=is_reposted,
        )

        return job_details_data
