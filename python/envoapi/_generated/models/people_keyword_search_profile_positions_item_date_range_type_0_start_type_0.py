from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PeopleKeywordSearchProfilePositionsItemDateRangeType0StartType0")


@_attrs_define
class PeopleKeywordSearchProfilePositionsItemDateRangeType0StartType0:
    """
    Attributes:
        year (int):
        month (int | None):
        day (int | None):
    """

    year: int
    month: int | None
    day: int | None

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month: int | None
        month = self.month

        day: int | None
        day = self.day

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "year": year,
                "month": month,
                "day": day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        def _parse_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        month = _parse_month(d.pop("month"))

        def _parse_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        day = _parse_day(d.pop("day"))

        people_keyword_search_profile_positions_item_date_range_type_0_start_type_0 = cls(
            year=year,
            month=month,
            day=day,
        )

        return people_keyword_search_profile_positions_item_date_range_type_0_start_type_0
