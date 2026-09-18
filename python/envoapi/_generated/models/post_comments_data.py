from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_comment import PostComment


T = TypeVar("T", bound="PostCommentsData")


@_attrs_define
class PostCommentsData:
    """
    Attributes:
        comments (list[PostComment]):
    """

    comments: list[PostComment]

    def to_dict(self) -> dict[str, Any]:
        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "comments": comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_comment import PostComment  # noqa: PLC0415

        d = dict(src_dict)
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = PostComment.from_dict(comments_item_data)

            comments.append(comments_item)

        post_comments_data = cls(
            comments=comments,
        )

        return post_comments_data
