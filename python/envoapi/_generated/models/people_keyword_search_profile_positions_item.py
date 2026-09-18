from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_profile_positions_item_date_range_type_0 import (
        PeopleKeywordSearchProfilePositionsItemDateRangeType0,
    )


T = TypeVar("T", bound="PeopleKeywordSearchProfilePositionsItem")


@_attrs_define
class PeopleKeywordSearchProfilePositionsItem:
    """
    Attributes:
        title (None | str):
        company_name (None | str):
        location (None | str):
        description (None | str):
        date_range (None | PeopleKeywordSearchProfilePositionsItemDateRangeType0):
    """

    title: None | str
    company_name: None | str
    location: None | str
    description: None | str
    date_range: None | PeopleKeywordSearchProfilePositionsItemDateRangeType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_keyword_search_profile_positions_item_date_range_type_0 import (
            PeopleKeywordSearchProfilePositionsItemDateRangeType0,  # noqa: PLC0415
        )

        title: None | str
        title = self.title

        company_name: None | str
        company_name = self.company_name

        location: None | str
        location = self.location

        description: None | str
        description = self.description

        date_range: dict[str, Any] | None
        if isinstance(self.date_range, PeopleKeywordSearchProfilePositionsItemDateRangeType0):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "companyName": company_name,
                "location": location,
                "description": description,
                "dateRange": date_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_keyword_search_profile_positions_item_date_range_type_0 import (
            PeopleKeywordSearchProfilePositionsItemDateRangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_company_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        company_name = _parse_company_name(d.pop("companyName"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_date_range(data: object) -> None | PeopleKeywordSearchProfilePositionsItemDateRangeType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                date_range_type_0 = PeopleKeywordSearchProfilePositionsItemDateRangeType0.from_dict(data)

                return date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleKeywordSearchProfilePositionsItemDateRangeType0, data)

        date_range = _parse_date_range(d.pop("dateRange"))

        people_keyword_search_profile_positions_item = cls(
            title=title,
            company_name=company_name,
            location=location,
            description=description,
            date_range=date_range,
        )

        return people_keyword_search_profile_positions_item
