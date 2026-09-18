from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BirthDateType0")


@_attrs_define
class BirthDateType0:
    """
    Attributes:
        year (int):
        month (None):
        day (None):
    """

    year: int
    month: None
    day: None

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
        if month is not None:
            raise TypeError("Expected null for month")

        day = d.pop("day")
        if day is not None:
            raise TypeError("Expected null for day")

        birth_date_type_0 = cls(
            year=year,
            month=month,
            day=day,
        )

        return birth_date_type_0
