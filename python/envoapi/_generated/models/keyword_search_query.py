from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeywordSearchQuery")


@_attrs_define
class KeywordSearchQuery:
    """
    Attributes:
        keywords (str):
        offset (int):  Default: 0.
    """

    keywords: str
    offset: int = 0

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        offset = d.pop("offset")

        keyword_search_query = cls(
            keywords=keywords,
            offset=offset,
        )

        return keyword_search_query
