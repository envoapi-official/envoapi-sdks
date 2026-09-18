from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_reference_type_0 import CompanyReferenceType0
    from ..models.company_reference_type_1 import CompanyReferenceType1
    from ..models.company_reference_type_2 import CompanyReferenceType2
    from ..models.date_range_type_0 import DateRangeType0
    from ..models.date_range_type_1 import DateRangeType1
    from ..models.employment_type import EmploymentType


T = TypeVar("T", bound="PositionItem")


@_attrs_define
class PositionItem:
    """
    Attributes:
        title (None | str):
        company (CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None):
        employment_type (EmploymentType | None):
        location (None | str):
        description (None | str):
        date_range (DateRangeType0 | DateRangeType1 | None):
    """

    title: None | str
    company: CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None
    employment_type: EmploymentType | None
    location: None | str
    description: None | str
    date_range: DateRangeType0 | DateRangeType1 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.company_reference_type_2 import CompanyReferenceType2  # noqa: PLC0415
        from ..models.date_range_type_0 import DateRangeType0  # noqa: PLC0415
        from ..models.date_range_type_1 import DateRangeType1  # noqa: PLC0415
        from ..models.employment_type import EmploymentType  # noqa: PLC0415

        title: None | str
        title = self.title

        company: dict[str, Any] | None
        if isinstance(self.company, CompanyReferenceType0):
            company = self.company.to_dict()
        elif isinstance(self.company, CompanyReferenceType1):
            company = self.company.to_dict()
        elif isinstance(self.company, CompanyReferenceType2):
            company = self.company.to_dict()
        else:
            company = self.company

        employment_type: dict[str, Any] | None
        if isinstance(self.employment_type, EmploymentType):
            employment_type = self.employment_type.to_dict()
        else:
            employment_type = self.employment_type

        location: None | str
        location = self.location

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
                "title": title,
                "company": company,
                "employmentType": employment_type,
                "location": location,
                "description": description,
                "dateRange": date_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.company_reference_type_2 import CompanyReferenceType2  # noqa: PLC0415
        from ..models.date_range_type_0 import DateRangeType0  # noqa: PLC0415
        from ..models.date_range_type_1 import DateRangeType1  # noqa: PLC0415
        from ..models.employment_type import EmploymentType  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_company(
            data: object,
        ) -> CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_reference_type_0 = CompanyReferenceType0.from_dict(data)

                return componentsschemas_company_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_reference_type_1 = CompanyReferenceType1.from_dict(data)

                return componentsschemas_company_reference_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_reference_type_2 = CompanyReferenceType2.from_dict(data)

                return componentsschemas_company_reference_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None, data)

        company = _parse_company(d.pop("company"))

        def _parse_employment_type(data: object) -> EmploymentType | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employment_type_type_0 = EmploymentType.from_dict(data)

                return employment_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmploymentType | None, data)

        employment_type = _parse_employment_type(d.pop("employmentType"))

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

        position_item = cls(
            title=title,
            company=company,
            employment_type=employment_type,
            location=location,
            description=description,
            date_range=date_range,
        )

        return position_item
