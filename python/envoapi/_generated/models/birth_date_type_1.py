from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="BirthDateType1")


@_attrs_define
class BirthDateType1:
    """
    Attributes:
        year (int | None):
        month (int):
        day (int | None):
    """

    year: int | None
    month: int
    day: int | None

    def to_dict(self) -> dict[str, Any]:
        year: int | None
        year = self.year

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

        def _parse_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        year = _parse_year(d.pop("year"))

        month = d.pop("month")

        def _parse_day(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        day = _parse_day(d.pop("day"))

        birth_date_type_1 = cls(
            year=year,
            month=month,
            day=day,
        )

        return birth_date_type_1
