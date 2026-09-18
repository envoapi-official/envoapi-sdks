from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_post import SearchPost


T = TypeVar("T", bound="SearchPostsData")


@_attrs_define
class SearchPostsData:
    """
    Attributes:
        posts (list[SearchPost]):
    """

    posts: list[SearchPost]

    def to_dict(self) -> dict[str, Any]:
        posts = []
        for posts_item_data in self.posts:
            posts_item = posts_item_data.to_dict()
            posts.append(posts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "posts": posts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_post import SearchPost  # noqa: PLC0415

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = SearchPost.from_dict(posts_item_data)

            posts.append(posts_item)

        search_posts_data = cls(
            posts=posts,
        )

        return search_posts_data
