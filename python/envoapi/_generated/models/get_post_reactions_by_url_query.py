from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_post_reactions_by_url_query_reaction_type import GetPostReactionsByUrlQueryReactionType

T = TypeVar("T", bound="GetPostReactionsByUrlQuery")


@_attrs_define
class GetPostReactionsByUrlQuery:
    """
    Attributes:
        url (str):
        reaction_type (GetPostReactionsByUrlQueryReactionType):
    """

    url: str
    reaction_type: GetPostReactionsByUrlQueryReactionType

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

        reaction_type = GetPostReactionsByUrlQueryReactionType(d.pop("reactionType"))

        get_post_reactions_by_url_query = cls(
            url=url,
            reaction_type=reaction_type,
        )

        return get_post_reactions_by_url_query
