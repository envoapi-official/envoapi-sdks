from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EmployeeCountRange")


@_attrs_define
class EmployeeCountRange:
    """
    Attributes:
        start (int):
        end (int | None):
    """

    start: int
    end: int | None

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end: int | None
        end = self.end

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        def _parse_end(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        end = _parse_end(d.pop("end"))

        employee_count_range = cls(
            start=start,
            end=end,
        )

        return employee_count_range
