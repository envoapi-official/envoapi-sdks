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


T = TypeVar("T", bound="VolunteerExperienceItem")


@_attrs_define
class VolunteerExperienceItem:
    """
    Attributes:
        role (None | str):
        organization (CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None):
        date_range (DateRangeType0 | DateRangeType1 | None):
        description (None | str):
    """

    role: None | str
    organization: CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2 | None
    date_range: DateRangeType0 | DateRangeType1 | None
    description: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.company_reference_type_2 import CompanyReferenceType2  # noqa: PLC0415
        from ..models.date_range_type_0 import DateRangeType0  # noqa: PLC0415
        from ..models.date_range_type_1 import DateRangeType1  # noqa: PLC0415

        role: None | str
        role = self.role

        organization: dict[str, Any] | None
        if isinstance(self.organization, CompanyReferenceType0):
            organization = self.organization.to_dict()
        elif isinstance(self.organization, CompanyReferenceType1):
            organization = self.organization.to_dict()
        elif isinstance(self.organization, CompanyReferenceType2):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        date_range: dict[str, Any] | None
        if isinstance(self.date_range, DateRangeType0):
            date_range = self.date_range.to_dict()
        elif isinstance(self.date_range, DateRangeType1):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        description: None | str
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
                "organization": organization,
                "dateRange": date_range,
                "description": description,
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

        d = dict(src_dict)

        def _parse_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        role = _parse_role(d.pop("role"))

        def _parse_organization(
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

        organization = _parse_organization(d.pop("organization"))

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

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        volunteer_experience_item = cls(
            role=role,
            organization=organization,
            date_range=date_range,
            description=description,
        )

        return volunteer_experience_item
