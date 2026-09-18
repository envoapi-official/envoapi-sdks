from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_post import ProfilePost


T = TypeVar("T", bound="ProfilePostsData")


@_attrs_define
class ProfilePostsData:
    """
    Attributes:
        posts (list[ProfilePost]):
    """

    posts: list[ProfilePost]

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
        from ..models.profile_post import ProfilePost  # noqa: PLC0415

        d = dict(src_dict)
        posts = []
        _posts = d.pop("posts")
        for posts_item_data in _posts:
            posts_item = ProfilePost.from_dict(posts_item_data)

            posts.append(posts_item)

        profile_posts_data = cls(
            posts=posts,
        )

        return profile_posts_data
