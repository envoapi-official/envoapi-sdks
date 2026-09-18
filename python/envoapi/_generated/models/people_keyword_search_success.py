from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_data import PeopleKeywordSearchData
    from ..models.people_keyword_search_success_meta import PeopleKeywordSearchSuccessMeta


T = TypeVar("T", bound="PeopleKeywordSearchSuccess")


@_attrs_define
class PeopleKeywordSearchSuccess:
    """
    Attributes:
        data (PeopleKeywordSearchData):
        meta (PeopleKeywordSearchSuccessMeta):
    """

    data: PeopleKeywordSearchData
    meta: PeopleKeywordSearchSuccessMeta

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
        from ..models.people_keyword_search_data import PeopleKeywordSearchData  # noqa: PLC0415
        from ..models.people_keyword_search_success_meta import PeopleKeywordSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = PeopleKeywordSearchData.from_dict(d.pop("data"))

        meta = PeopleKeywordSearchSuccessMeta.from_dict(d.pop("meta"))

        people_keyword_search_success = cls(
            data=data,
            meta=meta,
        )

        return people_keyword_search_success
