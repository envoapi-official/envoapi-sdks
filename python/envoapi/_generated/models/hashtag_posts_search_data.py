from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_post import CompanyPost


T = TypeVar("T", bound="HashtagPostsSearchData")


@_attrs_define
class HashtagPostsSearchData:
    """
    Attributes:
        posts (list[CompanyPost]):
    """

    posts: list[CompanyPost]

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
        from ..models.company_post import CompanyPost  # noqa: PLC0415

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = CompanyPost.from_dict(posts_item_data)

            posts.append(posts_item)

        hashtag_posts_search_data = cls(
            posts=posts,
        )

        return hashtag_posts_search_data
