from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.get_post_comments_by_url_query_sort_order import GetPostCommentsByUrlQuerySortOrder

T = TypeVar("T", bound="GetPostCommentsByUrlQuery")


@_attrs_define
class GetPostCommentsByUrlQuery:
    """
    Attributes:
        url (str):
        sort_order (GetPostCommentsByUrlQuerySortOrder):  Default: GetPostCommentsByUrlQuerySortOrder.CHRONOLOGICAL.
    """

    url: str
    sort_order: GetPostCommentsByUrlQuerySortOrder = GetPostCommentsByUrlQuerySortOrder.CHRONOLOGICAL

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

        sort_order = GetPostCommentsByUrlQuerySortOrder(d.pop("sortOrder"))

        get_post_comments_by_url_query = cls(
            url=url,
            sort_order=sort_order,
        )

        return get_post_comments_by_url_query
