from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.course_item import CourseItem


T = TypeVar("T", bound="ProfileCoursesData")


@_attrs_define
class ProfileCoursesData:
    """
    Attributes:
        courses (list[CourseItem]):
    """

    courses: list[CourseItem]

    def to_dict(self) -> dict[str, Any]:
        courses = []
        for componentsschemas_course_list_item_data in self.courses:
            componentsschemas_course_list_item = componentsschemas_course_list_item_data.to_dict()
            courses.append(componentsschemas_course_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "courses": courses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_item import CourseItem  # noqa: PLC0415

        d = dict(src_dict)
        courses = []
        _courses = d.pop("courses")
        for componentsschemas_course_list_item_data in _courses:
            componentsschemas_course_list_item = CourseItem.from_dict(componentsschemas_course_list_item_data)

            courses.append(componentsschemas_course_list_item)

        profile_courses_data = cls(
            courses=courses,
        )

        return profile_courses_data
