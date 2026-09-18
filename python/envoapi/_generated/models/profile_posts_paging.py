from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfilePostsPaging")


@_attrs_define
class ProfilePostsPaging:
    """
    Attributes:
        count (int):
        returned (int):
        has_more (bool):
        next_cursor (None | str):
    """

    count: int
    returned: int
    has_more: bool
    next_cursor: None | str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        returned = self.returned

        has_more = self.has_more

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "returned": returned,
                "hasMore": has_more,
                "nextCursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        returned = d.pop("returned")

        has_more = d.pop("hasMore")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        profile_posts_paging = cls(
            count=count,
            returned=returned,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        return profile_posts_paging
