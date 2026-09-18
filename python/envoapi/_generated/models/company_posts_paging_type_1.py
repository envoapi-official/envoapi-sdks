from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyPostsPagingType1")


@_attrs_define
class CompanyPostsPagingType1:
    """Legacy saved-result replay only. Newly fetched pages always include returned, hasMore, and nextCursor.

    Attributes:
        start (int):
        count (int):
    """

    start: int
    count: int

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        count = d.pop("count")

        company_posts_paging_type_1 = cls(
            start=start,
            count=count,
        )

        return company_posts_paging_type_1
