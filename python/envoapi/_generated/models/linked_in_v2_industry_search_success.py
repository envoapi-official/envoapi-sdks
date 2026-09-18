from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.industry_search_data import IndustrySearchData
    from ..models.linked_in_v2_industry_search_success_meta import LinkedInV2IndustrySearchSuccessMeta


T = TypeVar("T", bound="LinkedInV2IndustrySearchSuccess")


@_attrs_define
class LinkedInV2IndustrySearchSuccess:
    """
    Attributes:
        data (IndustrySearchData):
        meta (LinkedInV2IndustrySearchSuccessMeta):
    """

    data: IndustrySearchData
    meta: LinkedInV2IndustrySearchSuccessMeta

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
        from ..models.industry_search_data import IndustrySearchData  # noqa: PLC0415
        from ..models.linked_in_v2_industry_search_success_meta import (
            LinkedInV2IndustrySearchSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = IndustrySearchData.from_dict(d.pop("data"))

        meta = LinkedInV2IndustrySearchSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_industry_search_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_industry_search_success
