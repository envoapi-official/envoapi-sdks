from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_comment import ProfileComment


T = TypeVar("T", bound="ProfileCommentsData")


@_attrs_define
class ProfileCommentsData:
    """
    Attributes:
        comments (list[ProfileComment]):
    """

    comments: list[ProfileComment]

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
        from ..models.profile_comment import ProfileComment  # noqa: PLC0415

        d = dict(src_dict)
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = ProfileComment.from_dict(comments_item_data)

            comments.append(comments_item)

        profile_comments_data = cls(
            comments=comments,
        )

        return profile_comments_data
