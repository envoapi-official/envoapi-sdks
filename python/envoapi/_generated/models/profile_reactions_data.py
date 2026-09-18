from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_reaction import ProfileReaction


T = TypeVar("T", bound="ProfileReactionsData")


@_attrs_define
class ProfileReactionsData:
    """
    Attributes:
        reactions (list[ProfileReaction]):
    """

    reactions: list[ProfileReaction]

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
        from ..models.profile_reaction import ProfileReaction  # noqa: PLC0415

        d = dict(src_dict)
        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = ProfileReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        profile_reactions_data = cls(
            reactions=reactions,
        )

        return profile_reactions_data
