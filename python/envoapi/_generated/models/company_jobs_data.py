from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_job import CompanyJob
    from ..models.company_jobs_company import CompanyJobsCompany


T = TypeVar("T", bound="CompanyJobsData")


@_attrs_define
class CompanyJobsData:
    """
    Attributes:
        company (CompanyJobsCompany):
        jobs (list[CompanyJob]):
    """

    company: CompanyJobsCompany
    jobs: list[CompanyJob]

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company": company,
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_job import CompanyJob  # noqa: PLC0415
        from ..models.company_jobs_company import CompanyJobsCompany  # noqa: PLC0415

        d = dict(src_dict)
        company = CompanyJobsCompany.from_dict(d.pop("company"))

        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = CompanyJob.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        company_jobs_data = cls(
            company=company,
            jobs=jobs,
        )

        return company_jobs_data
