from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_job_filters_success_data import LinkedInV2JobFiltersSuccessData
    from ..models.linked_in_v2_job_filters_success_meta import LinkedInV2JobFiltersSuccessMeta


T = TypeVar("T", bound="LinkedInV2JobFiltersSuccess")


@_attrs_define
class LinkedInV2JobFiltersSuccess:
    """
    Attributes:
        data (LinkedInV2JobFiltersSuccessData):
        meta (LinkedInV2JobFiltersSuccessMeta):
    """

    data: LinkedInV2JobFiltersSuccessData
    meta: LinkedInV2JobFiltersSuccessMeta

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
        from ..models.linked_in_v2_job_filters_success_data import LinkedInV2JobFiltersSuccessData  # noqa: PLC0415
        from ..models.linked_in_v2_job_filters_success_meta import LinkedInV2JobFiltersSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = LinkedInV2JobFiltersSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2JobFiltersSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_job_filters_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_job_filters_success
