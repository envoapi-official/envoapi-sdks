from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LocationSearchQuery")


@_attrs_define
class LocationSearchQuery:
    """
    Attributes:
        keywords (str):
    """

    keywords: str

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        location_search_query = cls(
            keywords=keywords,
        )

        return location_search_query
