from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_post_comments_query_type_0_sort_order import LinkedInV2PostCommentsQueryType0SortOrder

T = TypeVar("T", bound="LinkedInV2PostCommentsQueryType0")


@_attrs_define
class LinkedInV2PostCommentsQueryType0:
    """
    Attributes:
        slug (str):
        sort_order (LinkedInV2PostCommentsQueryType0SortOrder):  Default:
            LinkedInV2PostCommentsQueryType0SortOrder.CHRONOLOGICAL.
    """

    slug: str
    sort_order: LinkedInV2PostCommentsQueryType0SortOrder = LinkedInV2PostCommentsQueryType0SortOrder.CHRONOLOGICAL

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "sortOrder": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        sort_order = LinkedInV2PostCommentsQueryType0SortOrder(d.pop("sortOrder"))

        linked_in_v2_post_comments_query_type_0 = cls(
            slug=slug,
            sort_order=sort_order,
        )

        return linked_in_v2_post_comments_query_type_0
