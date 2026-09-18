from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_profile_education_item_date_range_type_0 import (
        PeopleKeywordSearchProfileEducationItemDateRangeType0,
    )


T = TypeVar("T", bound="PeopleKeywordSearchProfileEducationItem")


@_attrs_define
class PeopleKeywordSearchProfileEducationItem:
    """
    Attributes:
        school_name (None | str):
        degree_name (None | str):
        field_of_study (None | str):
        date_range (None | PeopleKeywordSearchProfileEducationItemDateRangeType0):
    """

    school_name: None | str
    degree_name: None | str
    field_of_study: None | str
    date_range: None | PeopleKeywordSearchProfileEducationItemDateRangeType0

    def to_dict(self) -> dict[str, Any]:
        from ..models.people_keyword_search_profile_education_item_date_range_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0,  # noqa: PLC0415
        )

        school_name: None | str
        school_name = self.school_name

        degree_name: None | str
        degree_name = self.degree_name

        field_of_study: None | str
        field_of_study = self.field_of_study

        date_range: dict[str, Any] | None
        if isinstance(self.date_range, PeopleKeywordSearchProfileEducationItemDateRangeType0):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "schoolName": school_name,
                "degreeName": degree_name,
                "fieldOfStudy": field_of_study,
                "dateRange": date_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_keyword_search_profile_education_item_date_range_type_0 import (
            PeopleKeywordSearchProfileEducationItemDateRangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_school_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        school_name = _parse_school_name(d.pop("schoolName"))

        def _parse_degree_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        degree_name = _parse_degree_name(d.pop("degreeName"))

        def _parse_field_of_study(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy"))

        def _parse_date_range(data: object) -> None | PeopleKeywordSearchProfileEducationItemDateRangeType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                date_range_type_0 = PeopleKeywordSearchProfileEducationItemDateRangeType0.from_dict(data)

                return date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PeopleKeywordSearchProfileEducationItemDateRangeType0, data)

        date_range = _parse_date_range(d.pop("dateRange"))

        people_keyword_search_profile_education_item = cls(
            school_name=school_name,
            degree_name=degree_name,
            field_of_study=field_of_study,
            date_range=date_range,
        )

        return people_keyword_search_profile_education_item
