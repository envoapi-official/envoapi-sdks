from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_company_similar_success_data import LinkedInV2CompanySimilarSuccessData
    from ..models.linked_in_v2_company_similar_success_meta import LinkedInV2CompanySimilarSuccessMeta


T = TypeVar("T", bound="LinkedInV2CompanySimilarSuccess")


@_attrs_define
class LinkedInV2CompanySimilarSuccess:
    """
    Attributes:
        data (LinkedInV2CompanySimilarSuccessData):
        meta (LinkedInV2CompanySimilarSuccessMeta):
    """

    data: LinkedInV2CompanySimilarSuccessData
    meta: LinkedInV2CompanySimilarSuccessMeta

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
        from ..models.linked_in_v2_company_similar_success_data import (
            LinkedInV2CompanySimilarSuccessData,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_company_similar_success_meta import (
            LinkedInV2CompanySimilarSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LinkedInV2CompanySimilarSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2CompanySimilarSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_company_similar_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_company_similar_success
