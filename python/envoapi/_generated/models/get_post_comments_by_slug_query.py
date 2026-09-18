from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_post_comments_by_slug_query_sort_order import GetPostCommentsBySlugQuerySortOrder

T = TypeVar("T", bound="GetPostCommentsBySlugQuery")


@_attrs_define
class GetPostCommentsBySlugQuery:
    """
    Attributes:
        slug (str):
        sort_order (GetPostCommentsBySlugQuerySortOrder):  Default: GetPostCommentsBySlugQuerySortOrder.CHRONOLOGICAL.
    """

    slug: str
    sort_order: GetPostCommentsBySlugQuerySortOrder = GetPostCommentsBySlugQuerySortOrder.CHRONOLOGICAL

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

        sort_order = GetPostCommentsBySlugQuerySortOrder(d.pop("sortOrder"))

        get_post_comments_by_slug_query = cls(
            slug=slug,
            sort_order=sort_order,
        )

        return get_post_comments_by_slug_query
