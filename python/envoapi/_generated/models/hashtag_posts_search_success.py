from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.hashtag_posts_search_data import HashtagPostsSearchData
    from ..models.hashtag_posts_search_success_meta import HashtagPostsSearchSuccessMeta


T = TypeVar("T", bound="HashtagPostsSearchSuccess")


@_attrs_define
class HashtagPostsSearchSuccess:
    """
    Attributes:
        data (HashtagPostsSearchData):
        meta (HashtagPostsSearchSuccessMeta):
    """

    data: HashtagPostsSearchData
    meta: HashtagPostsSearchSuccessMeta

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
        from ..models.hashtag_posts_search_data import HashtagPostsSearchData  # noqa: PLC0415
        from ..models.hashtag_posts_search_success_meta import HashtagPostsSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = HashtagPostsSearchData.from_dict(d.pop("data"))

        meta = HashtagPostsSearchSuccessMeta.from_dict(d.pop("meta"))

        hashtag_posts_search_success = cls(
            data=data,
            meta=meta,
        )

        return hashtag_posts_search_success
