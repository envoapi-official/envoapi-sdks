from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="HashtagPostsSearchPaging")


@_attrs_define
class HashtagPostsSearchPaging:
    """
    Attributes:
        offset (int):
        limit (int):
        returned (int):
        total (int):
        has_more (bool):
        next_offset (int | None):
    """

    offset: int
    limit: int
    returned: int
    total: int
    has_more: bool
    next_offset: int | None

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        returned = self.returned

        total = self.total

        has_more = self.has_more

        next_offset: int | None
        next_offset = self.next_offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "returned": returned,
                "total": total,
                "hasMore": has_more,
                "nextOffset": next_offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        returned = d.pop("returned")

        total = d.pop("total")

        has_more = d.pop("hasMore")

        def _parse_next_offset(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_offset = _parse_next_offset(d.pop("nextOffset"))

        hashtag_posts_search_paging = cls(
            offset=offset,
            limit=limit,
            returned=returned,
            total=total,
            has_more=has_more,
            next_offset=next_offset,
        )

        return hashtag_posts_search_paging
