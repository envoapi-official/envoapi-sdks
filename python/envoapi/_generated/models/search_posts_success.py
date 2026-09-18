from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_posts_data import SearchPostsData
    from ..models.search_posts_success_meta import SearchPostsSuccessMeta


T = TypeVar("T", bound="SearchPostsSuccess")


@_attrs_define
class SearchPostsSuccess:
    """
    Attributes:
        data (SearchPostsData):
        meta (SearchPostsSuccessMeta):
    """

    data: SearchPostsData
    meta: SearchPostsSuccessMeta

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
        from ..models.search_posts_data import SearchPostsData  # noqa: PLC0415
        from ..models.search_posts_success_meta import SearchPostsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = SearchPostsData.from_dict(d.pop("data"))

        meta = SearchPostsSuccessMeta.from_dict(d.pop("meta"))

        search_posts_success = cls(
            data=data,
            meta=meta,
        )

        return search_posts_success
