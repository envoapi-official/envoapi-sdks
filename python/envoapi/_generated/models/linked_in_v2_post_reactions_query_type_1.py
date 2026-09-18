from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_post_reactions_query_type_1_reaction_type import (
    LinkedInV2PostReactionsQueryType1ReactionType,
)

T = TypeVar("T", bound="LinkedInV2PostReactionsQueryType1")


@_attrs_define
class LinkedInV2PostReactionsQueryType1:
    """
    Attributes:
        url (str):
        reaction_type (LinkedInV2PostReactionsQueryType1ReactionType):
    """

    url: str
    reaction_type: LinkedInV2PostReactionsQueryType1ReactionType

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        reaction_type = self.reaction_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "reactionType": reaction_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        reaction_type = LinkedInV2PostReactionsQueryType1ReactionType(d.pop("reactionType"))

        linked_in_v2_post_reactions_query_type_1 = cls(
            url=url,
            reaction_type=reaction_type,
        )

        return linked_in_v2_post_reactions_query_type_1
