from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PartialDateType1")


@_attrs_define
class PartialDateType1:
    """
    Attributes:
        year (int):
        month (int):
        day (int):
    """

    year: int
    month: int
    day: int

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        month = self.month

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

        month = d.pop("month")

        day = d.pop("day")

        partial_date_type_1 = cls(
            year=year,
            month=month,
            day=day,
        )

        return partial_date_type_1
