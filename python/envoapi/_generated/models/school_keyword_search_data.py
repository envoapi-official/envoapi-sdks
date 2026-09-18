from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.school_keyword_search_school import SchoolKeywordSearchSchool


T = TypeVar("T", bound="SchoolKeywordSearchData")


@_attrs_define
class SchoolKeywordSearchData:
    """
    Attributes:
        schools (list[SchoolKeywordSearchSchool]):
    """

    schools: list[SchoolKeywordSearchSchool]

    def to_dict(self) -> dict[str, Any]:
        schools = []
        for schools_item_data in self.schools:
            schools_item = schools_item_data.to_dict()
            schools.append(schools_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "schools": schools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.school_keyword_search_school import SchoolKeywordSearchSchool  # noqa: PLC0415

        d = dict(src_dict)
        schools = []
        _schools = d.pop("schools")
        for schools_item_data in _schools:
            schools_item = SchoolKeywordSearchSchool.from_dict(schools_item_data)

            schools.append(schools_item)

        school_keyword_search_data = cls(
            schools=schools,
        )

        return school_keyword_search_data
