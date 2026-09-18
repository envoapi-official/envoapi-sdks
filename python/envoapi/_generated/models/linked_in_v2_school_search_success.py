from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_school_search_success_meta import LinkedInV2SchoolSearchSuccessMeta
    from ..models.school_keyword_search_data import SchoolKeywordSearchData


T = TypeVar("T", bound="LinkedInV2SchoolSearchSuccess")


@_attrs_define
class LinkedInV2SchoolSearchSuccess:
    """
    Attributes:
        data (SchoolKeywordSearchData):
        meta (LinkedInV2SchoolSearchSuccessMeta):
    """

    data: SchoolKeywordSearchData
    meta: LinkedInV2SchoolSearchSuccessMeta

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
        from ..models.linked_in_v2_school_search_success_meta import LinkedInV2SchoolSearchSuccessMeta  # noqa: PLC0415
        from ..models.school_keyword_search_data import SchoolKeywordSearchData  # noqa: PLC0415

        d = dict(src_dict)
        data = SchoolKeywordSearchData.from_dict(d.pop("data"))

        meta = LinkedInV2SchoolSearchSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_school_search_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_school_search_success
