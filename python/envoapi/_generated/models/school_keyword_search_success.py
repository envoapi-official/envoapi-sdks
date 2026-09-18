from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.school_keyword_search_data import SchoolKeywordSearchData
    from ..models.school_keyword_search_success_meta import SchoolKeywordSearchSuccessMeta


T = TypeVar("T", bound="SchoolKeywordSearchSuccess")


@_attrs_define
class SchoolKeywordSearchSuccess:
    """
    Attributes:
        data (SchoolKeywordSearchData):
        meta (SchoolKeywordSearchSuccessMeta):
    """

    data: SchoolKeywordSearchData
    meta: SchoolKeywordSearchSuccessMeta

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
        from ..models.school_keyword_search_data import SchoolKeywordSearchData  # noqa: PLC0415
        from ..models.school_keyword_search_success_meta import SchoolKeywordSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = SchoolKeywordSearchData.from_dict(d.pop("data"))

        meta = SchoolKeywordSearchSuccessMeta.from_dict(d.pop("meta"))

        school_keyword_search_success = cls(
            data=data,
            meta=meta,
        )

        return school_keyword_search_success
