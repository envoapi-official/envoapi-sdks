from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partial_date_type_0 import PartialDateType0
    from ..models.partial_date_type_1 import PartialDateType1


T = TypeVar("T", bound="DateRangeType1")


@_attrs_define
class DateRangeType1:
    """
    Attributes:
        start (None | PartialDateType0 | PartialDateType1):
        end (None | PartialDateType0 | PartialDateType1):
        is_current (bool | None):
    """

    start: None | PartialDateType0 | PartialDateType1
    end: None | PartialDateType0 | PartialDateType1
    is_current: bool | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415

        start: dict[str, Any] | None
        if isinstance(self.start, PartialDateType0):
            start = self.start.to_dict()
        elif isinstance(self.start, PartialDateType1):
            start = self.start.to_dict()
        else:
            start = self.start

        end: dict[str, Any] | None
        if isinstance(self.end, PartialDateType0):
            end = self.end.to_dict()
        elif isinstance(self.end, PartialDateType1):
            end = self.end.to_dict()
        else:
            end = self.end

        is_current: bool | None
        is_current = self.is_current

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "end": end,
                "isCurrent": is_current,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_start(data: object) -> None | PartialDateType0 | PartialDateType1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_0 = PartialDateType0.from_dict(data)

                return componentsschemas_partial_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_1 = PartialDateType1.from_dict(data)

                return componentsschemas_partial_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartialDateType0 | PartialDateType1, data)

        start = _parse_start(d.pop("start"))

        def _parse_end(data: object) -> None | PartialDateType0 | PartialDateType1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_0 = PartialDateType0.from_dict(data)

                return componentsschemas_partial_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_1 = PartialDateType1.from_dict(data)

                return componentsschemas_partial_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartialDateType0 | PartialDateType1, data)

        end = _parse_end(d.pop("end"))

        def _parse_is_current(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_current = _parse_is_current(d.pop("isCurrent"))

        date_range_type_1 = cls(
            start=start,
            end=end,
            is_current=is_current,
        )

        return date_range_type_1
