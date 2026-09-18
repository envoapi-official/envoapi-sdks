from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.post_reaction_count_type import PostReactionCountType

T = TypeVar("T", bound="PostReactionCount")


@_attrs_define
class PostReactionCount:
    """
    Attributes:
        type_ (PostReactionCountType):
        count (int):
    """

    type_: PostReactionCountType
    count: int

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PostReactionCountType(d.pop("type"))

        count = d.pop("count")

        post_reaction_count = cls(
            type_=type_,
            count=count,
        )

        return post_reaction_count
