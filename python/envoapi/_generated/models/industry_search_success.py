from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.industry_search_data import IndustrySearchData
    from ..models.industry_search_success_meta import IndustrySearchSuccessMeta


T = TypeVar("T", bound="IndustrySearchSuccess")


@_attrs_define
class IndustrySearchSuccess:
    """
    Attributes:
        data (IndustrySearchData):
        meta (IndustrySearchSuccessMeta):
    """

    data: IndustrySearchData
    meta: IndustrySearchSuccessMeta

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
        from ..models.industry_search_success_meta import IndustrySearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = IndustrySearchData.from_dict(d.pop("data"))

        meta = IndustrySearchSuccessMeta.from_dict(d.pop("meta"))

        industry_search_success = cls(
            data=data,
            meta=meta,
        )

        return industry_search_success
