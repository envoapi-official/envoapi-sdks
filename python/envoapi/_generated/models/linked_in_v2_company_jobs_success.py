from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_jobs_data import CompanyJobsData
    from ..models.linked_in_v2_company_jobs_success_meta import LinkedInV2CompanyJobsSuccessMeta


T = TypeVar("T", bound="LinkedInV2CompanyJobsSuccess")


@_attrs_define
class LinkedInV2CompanyJobsSuccess:
    """
    Attributes:
        data (CompanyJobsData):
        meta (LinkedInV2CompanyJobsSuccessMeta):
    """

    data: CompanyJobsData
    meta: LinkedInV2CompanyJobsSuccessMeta

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_jobs_data import CompanyJobsData  # noqa: PLC0415
        from ..models.linked_in_v2_company_jobs_success_meta import LinkedInV2CompanyJobsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyJobsData.from_dict(d.pop("data"))

        meta = LinkedInV2CompanyJobsSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_company_jobs_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_company_jobs_success
