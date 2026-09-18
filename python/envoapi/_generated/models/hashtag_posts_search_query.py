from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HashtagPostsSearchQuery")


@_attrs_define
class HashtagPostsSearchQuery:
    """
    Attributes:
        hashtag (str):
        offset (int):  Default: 0.
    """

    hashtag: str
    offset: int = 0

    def to_dict(self) -> dict[str, Any]:
        hashtag = self.hashtag

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hashtag": hashtag,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hashtag = d.pop("hashtag")
        if not isinstance(hashtag, str):
            raise TypeError("Expected string for hashtag")

        offset = d.pop("offset")

        hashtag_posts_search_query = cls(
            hashtag=hashtag,
            offset=offset,
        )

        return hashtag_posts_search_query
