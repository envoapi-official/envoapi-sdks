from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.job_details_data import JobDetailsData
    from ..models.job_details_success_meta import JobDetailsSuccessMeta


T = TypeVar("T", bound="JobDetailsSuccess")


@_attrs_define
class JobDetailsSuccess:
    """
    Attributes:
        data (JobDetailsData):
        meta (JobDetailsSuccessMeta):
    """

    data: JobDetailsData
    meta: JobDetailsSuccessMeta

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
        from ..models.job_details_data import JobDetailsData  # noqa: PLC0415
        from ..models.job_details_success_meta import JobDetailsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = JobDetailsData.from_dict(d.pop("data"))

        meta = JobDetailsSuccessMeta.from_dict(d.pop("meta"))

        job_details_success = cls(
            data=data,
            meta=meta,
        )

        return job_details_success
