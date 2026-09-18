from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_reaction import PostReaction


T = TypeVar("T", bound="PostReactionsData")


@_attrs_define
class PostReactionsData:
    """
    Attributes:
        reactions (list[PostReaction]):
    """

    reactions: list[PostReaction]

    def to_dict(self) -> dict[str, Any]:
        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reactions": reactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_reaction import PostReaction  # noqa: PLC0415

        d = dict(src_dict)
        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = PostReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        post_reactions_data = cls(
            reactions=reactions,
        )

        return post_reactions_data
