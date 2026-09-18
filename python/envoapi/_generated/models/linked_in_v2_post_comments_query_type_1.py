from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_post_comments_query_type_1_sort_order import LinkedInV2PostCommentsQueryType1SortOrder

T = TypeVar("T", bound="LinkedInV2PostCommentsQueryType1")


@_attrs_define
class LinkedInV2PostCommentsQueryType1:
    """
    Attributes:
        url (str):
        sort_order (LinkedInV2PostCommentsQueryType1SortOrder):  Default:
            LinkedInV2PostCommentsQueryType1SortOrder.CHRONOLOGICAL.
    """

    url: str
    sort_order: LinkedInV2PostCommentsQueryType1SortOrder = LinkedInV2PostCommentsQueryType1SortOrder.CHRONOLOGICAL

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "sortOrder": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        sort_order = LinkedInV2PostCommentsQueryType1SortOrder(d.pop("sortOrder"))

        linked_in_v2_post_comments_query_type_1 = cls(
            url=url,
            sort_order=sort_order,
        )

        return linked_in_v2_post_comments_query_type_1
