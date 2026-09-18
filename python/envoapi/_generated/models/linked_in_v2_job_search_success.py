from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.job_search_data import JobSearchData
    from ..models.linked_in_v2_job_search_success_meta import LinkedInV2JobSearchSuccessMeta


T = TypeVar("T", bound="LinkedInV2JobSearchSuccess")


@_attrs_define
class LinkedInV2JobSearchSuccess:
    """
    Attributes:
        data (JobSearchData):
        meta (LinkedInV2JobSearchSuccessMeta):
    """

    data: JobSearchData
    meta: LinkedInV2JobSearchSuccessMeta

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
        from ..models.job_search_data import JobSearchData  # noqa: PLC0415
        from ..models.linked_in_v2_job_search_success_meta import LinkedInV2JobSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = JobSearchData.from_dict(d.pop("data"))

        meta = LinkedInV2JobSearchSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_job_search_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_job_search_success
