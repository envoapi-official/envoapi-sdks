from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_typeahead_data import SearchTypeaheadData
    from ..models.search_typeahead_success_meta import SearchTypeaheadSuccessMeta


T = TypeVar("T", bound="SearchTypeaheadSuccess")


@_attrs_define
class SearchTypeaheadSuccess:
    """
    Attributes:
        data (SearchTypeaheadData):
        meta (SearchTypeaheadSuccessMeta):
    """

    data: SearchTypeaheadData
    meta: SearchTypeaheadSuccessMeta

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
        from ..models.search_typeahead_data import SearchTypeaheadData  # noqa: PLC0415
        from ..models.search_typeahead_success_meta import SearchTypeaheadSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = SearchTypeaheadData.from_dict(d.pop("data"))

        meta = SearchTypeaheadSuccessMeta.from_dict(d.pop("meta"))

        search_typeahead_success = cls(
            data=data,
            meta=meta,
        )

        return search_typeahead_success
