from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.keyword_search_data import KeywordSearchData
    from ..models.keyword_search_success_meta import KeywordSearchSuccessMeta


T = TypeVar("T", bound="KeywordSearchSuccess")


@_attrs_define
class KeywordSearchSuccess:
    """
    Attributes:
        data (KeywordSearchData):
        meta (KeywordSearchSuccessMeta):
    """

    data: KeywordSearchData
    meta: KeywordSearchSuccessMeta

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
        from ..models.keyword_search_data import KeywordSearchData  # noqa: PLC0415
        from ..models.keyword_search_success_meta import KeywordSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = KeywordSearchData.from_dict(d.pop("data"))

        meta = KeywordSearchSuccessMeta.from_dict(d.pop("meta"))

        keyword_search_success = cls(
            data=data,
            meta=meta,
        )

        return keyword_search_success
