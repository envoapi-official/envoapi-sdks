from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileCompanyInterestsPaging")


@_attrs_define
class ProfileCompanyInterestsPaging:
    """
    Attributes:
        start (int):
        count (int):
        returned (int):
        has_more (bool):
        next_start (int | None):
    """

    start: int
    count: int
    returned: int
    has_more: bool
    next_start: int | None

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        count = self.count

        returned = self.returned

        has_more = self.has_more

        next_start: int | None
        next_start = self.next_start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "count": count,
                "returned": returned,
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

        has_more = d.pop("hasMore")

        def _parse_next_start(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_start = _parse_next_start(d.pop("nextStart"))

        profile_company_interests_paging = cls(
            start=start,
            count=count,
            returned=returned,
            has_more=has_more,
            next_start=next_start,
        )

        return profile_company_interests_paging
