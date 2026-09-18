from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_profile_education_item_date_range_type_0_end_type_0 import (
        PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0,
    )
    from ..models.people_keyword_search_profile_education_item_date_range_type_0_start_type_0 import (
        PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0,
    )


T = TypeVar("T", bound="PeopleKeywordSearchProfileEducationItemDateRangeType0")


@_attrs_define
class PeopleKeywordSearchProfileEducationItemDateRangeType0:
    """
    Attributes:
        start (None | PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0):
        end (None | PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0):
        is_current (bool | None):
    """

    start: None | PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0
    end: None | PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0
    is_current: bool | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_keyword_search_profile_education_item_date_range_type_0_end_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0,  # noqa: PLC0415
        )
        from ..models.people_keyword_search_profile_education_item_date_range_type_0_start_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0,  # noqa: PLC0415
        )

        start: dict[str, Any] | None
        if isinstance(self.start, PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0):
            start = self.start.to_dict()
        else:
            start = self.start

        end: dict[str, Any] | None
        if isinstance(self.end, PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0):
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
        from ..models.people_keyword_search_profile_education_item_date_range_type_0_end_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0,  # noqa: PLC0415
        )
        from ..models.people_keyword_search_profile_education_item_date_range_type_0_start_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_start(data: object) -> None | PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                start_type_0 = PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0.from_dict(data)

                return start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleKeywordSearchProfileEducationItemDateRangeType0StartType0, data)

        start = _parse_start(d.pop("start"))

        def _parse_end(data: object) -> None | PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                end_type_0 = PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0.from_dict(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleKeywordSearchProfileEducationItemDateRangeType0EndType0, data)

        end = _parse_end(d.pop("end"))

        def _parse_is_current(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_current = _parse_is_current(d.pop("isCurrent"))

        people_keyword_search_profile_education_item_date_range_type_0 = cls(
            start=start,
            end=end,
            is_current=is_current,
        )

        return people_keyword_search_profile_education_item_date_range_type_0
