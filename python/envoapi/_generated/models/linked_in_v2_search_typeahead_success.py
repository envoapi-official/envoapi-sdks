from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_search_typeahead_success_meta import LinkedInV2SearchTypeaheadSuccessMeta
    from ..models.search_typeahead_data import SearchTypeaheadData


T = TypeVar("T", bound="LinkedInV2SearchTypeaheadSuccess")


@_attrs_define
class LinkedInV2SearchTypeaheadSuccess:
    """
    Attributes:
        data (SearchTypeaheadData):
        meta (LinkedInV2SearchTypeaheadSuccessMeta):
    """

    data: SearchTypeaheadData
    meta: LinkedInV2SearchTypeaheadSuccessMeta

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
        from ..models.linked_in_v2_search_typeahead_success_meta import (
            LinkedInV2SearchTypeaheadSuccessMeta,  # noqa: PLC0415
        )
        from ..models.search_typeahead_data import SearchTypeaheadData  # noqa: PLC0415

        d = dict(src_dict)
        data = SearchTypeaheadData.from_dict(d.pop("data"))

        meta = LinkedInV2SearchTypeaheadSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_search_typeahead_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_search_typeahead_success
