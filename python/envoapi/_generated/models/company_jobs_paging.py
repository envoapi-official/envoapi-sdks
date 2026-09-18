from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyJobsPaging")


@_attrs_define
class CompanyJobsPaging:
    """
    Attributes:
        start (int):
        count (int): Effective page size, reduced when necessary to stay within the first 1,000 results.
        returned (int): Number of jobs returned on this page.
        total (int):
        has_more (bool):
        next_start (int | None): Use as the next request's start; null when there is no next accessible page. Pages can
            shift or overlap; deduplicate collected jobs by URL.
    """

    start: int
    count: int
    returned: int
    total: int
    has_more: bool
    next_start: int | None

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        count = self.count

        returned = self.returned

        total = self.total

        has_more = self.has_more

        next_start: int | None
        next_start = self.next_start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "count": count,
                "returned": returned,
                "total": total,
                "hasMore": has_more,
                "nextStart": next_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        count = d.pop("count")

        returned = d.pop("returned")

        total = d.pop("total")

        has_more = d.pop("hasMore")

        def _parse_next_start(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_start = _parse_next_start(d.pop("nextStart"))

        company_jobs_paging = cls(
            start=start,
            count=count,
            returned=returned,
            total=total,
            has_more=has_more,
            next_start=next_start,
        )

        return company_jobs_paging
