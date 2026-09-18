from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.date_range_type_0 import DateRangeType0
    from ..models.date_range_type_1 import DateRangeType1
    from ..models.school_reference_type_0 import SchoolReferenceType0
    from ..models.school_reference_type_1 import SchoolReferenceType1
    from ..models.school_reference_type_2 import SchoolReferenceType2


T = TypeVar("T", bound="EducationItem")


@_attrs_define
class EducationItem:
    """
    Attributes:
        school (None | SchoolReferenceType0 | SchoolReferenceType1 | SchoolReferenceType2):
        degree (None | str):
        field_of_study (None | str):
        grade (None | str):
        activities (None | str):
        description (None | str):
        date_range (DateRangeType0 | DateRangeType1 | None):
    """

    school: None | SchoolReferenceType0 | SchoolReferenceType1 | SchoolReferenceType2
    degree: None | str
    field_of_study: None | str
    grade: None | str
    activities: None | str
    description: None | str
    date_range: DateRangeType0 | DateRangeType1 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.date_range_type_0 import DateRangeType0  # noqa: PLC0415
        from ..models.date_range_type_1 import DateRangeType1  # noqa: PLC0415
        from ..models.school_reference_type_0 import SchoolReferenceType0  # noqa: PLC0415
        from ..models.school_reference_type_1 import SchoolReferenceType1  # noqa: PLC0415
        from ..models.school_reference_type_2 import SchoolReferenceType2  # noqa: PLC0415

        school: dict[str, Any] | None
        if isinstance(self.school, SchoolReferenceType0):
            school = self.school.to_dict()
        elif isinstance(self.school, SchoolReferenceType1):
            school = self.school.to_dict()
        elif isinstance(self.school, SchoolReferenceType2):
            school = self.school.to_dict()
        else:
            school = self.school

        degree: None | str
        degree = self.degree

        field_of_study: None | str
        field_of_study = self.field_of_study

        grade: None | str
        grade = self.grade

        activities: None | str
        activities = self.activities

        description: None | str
        description = self.description

        date_range: dict[str, Any] | None
        if isinstance(self.date_range, DateRangeType0):
            date_range = self.date_range.to_dict()
        elif isinstance(self.date_range, DateRangeType1):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "school": school,
                "degree": degree,
                "fieldOfStudy": field_of_study,
                "grade": grade,
                "activities": activities,
                "description": description,
                "dateRange": date_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range_type_0 import DateRangeType0  # noqa: PLC0415
        from ..models.date_range_type_1 import DateRangeType1  # noqa: PLC0415
        from ..models.school_reference_type_0 import SchoolReferenceType0  # noqa: PLC0415
        from ..models.school_reference_type_1 import SchoolReferenceType1  # noqa: PLC0415
        from ..models.school_reference_type_2 import SchoolReferenceType2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_school(data: object) -> None | SchoolReferenceType0 | SchoolReferenceType1 | SchoolReferenceType2:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_school_reference_type_0 = SchoolReferenceType0.from_dict(data)

                return componentsschemas_school_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_school_reference_type_1 = SchoolReferenceType1.from_dict(data)

                return componentsschemas_school_reference_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_school_reference_type_2 = SchoolReferenceType2.from_dict(data)

                return componentsschemas_school_reference_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SchoolReferenceType0 | SchoolReferenceType1 | SchoolReferenceType2, data)

        school = _parse_school(d.pop("school"))

        def _parse_degree(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        degree = _parse_degree(d.pop("degree"))

        def _parse_field_of_study(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field_of_study = _parse_field_of_study(d.pop("fieldOfStudy"))

        def _parse_grade(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grade = _parse_grade(d.pop("grade"))

        def _parse_activities(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        activities = _parse_activities(d.pop("activities"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_date_range(data: object) -> DateRangeType0 | DateRangeType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_date_range_type_0 = DateRangeType0.from_dict(data)

                return componentsschemas_date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_date_range_type_1 = DateRangeType1.from_dict(data)

                return componentsschemas_date_range_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DateRangeType0 | DateRangeType1 | None, data)

        date_range = _parse_date_range(d.pop("dateRange"))

        education_item = cls(
            school=school,
            degree=degree,
            field_of_study=field_of_study,
            grade=grade,
            activities=activities,
            description=description,
            date_range=date_range,
        )

        return education_item
