from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_post_reactions_by_slug_query_reaction_type import GetPostReactionsBySlugQueryReactionType

T = TypeVar("T", bound="GetPostReactionsBySlugQuery")


@_attrs_define
class GetPostReactionsBySlugQuery:
    """
    Attributes:
        slug (str):
        reaction_type (GetPostReactionsBySlugQueryReactionType):
    """

    slug: str
    reaction_type: GetPostReactionsBySlugQueryReactionType

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

        reaction_type = GetPostReactionsBySlugQueryReactionType(d.pop("reactionType"))

        get_post_reactions_by_slug_query = cls(
            slug=slug,
            reaction_type=reaction_type,
        )

        return get_post_reactions_by_slug_query
