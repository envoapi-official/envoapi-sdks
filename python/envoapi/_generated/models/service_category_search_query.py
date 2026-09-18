from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServiceCategorySearchQuery")


@_attrs_define
class ServiceCategorySearchQuery:
    """
    Attributes:
        query (str):  Default: ''.
    """

    query: str = ""

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")
        if not isinstance(query, str):
            raise TypeError("Expected string for query")

        service_category_search_query = cls(
            query=query,
        )

        return service_category_search_query
