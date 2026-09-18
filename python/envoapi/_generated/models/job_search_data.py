from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.job_search_job import JobSearchJob


T = TypeVar("T", bound="JobSearchData")


@_attrs_define
class JobSearchData:
    """
    Attributes:
        jobs (list[JobSearchJob]):
    """

    jobs: list[JobSearchJob]

    def to_dict(self) -> dict[str, Any]:
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_search_job import JobSearchJob  # noqa: PLC0415

        d = dict(src_dict)
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = JobSearchJob.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        job_search_data = cls(
            jobs=jobs,
        )

        return job_search_data
