from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_post_reactions_query_type_0_reaction_type import (
    LinkedInV2PostReactionsQueryType0ReactionType,
)

T = TypeVar("T", bound="LinkedInV2PostReactionsQueryType0")


@_attrs_define
class LinkedInV2PostReactionsQueryType0:
    """
    Attributes:
        slug (str):
        reaction_type (LinkedInV2PostReactionsQueryType0ReactionType):
    """

    slug: str
    reaction_type: LinkedInV2PostReactionsQueryType0ReactionType

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        reaction_type = self.reaction_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "reactionType": reaction_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        reaction_type = LinkedInV2PostReactionsQueryType0ReactionType(d.pop("reactionType"))

        linked_in_v2_post_reactions_query_type_0 = cls(
            slug=slug,
            reaction_type=reaction_type,
        )

        return linked_in_v2_post_reactions_query_type_0
