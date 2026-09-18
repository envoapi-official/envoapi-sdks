from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_reference_type_0 import CompanyReferenceType0
    from ..models.company_reference_type_1 import CompanyReferenceType1
    from ..models.company_reference_type_2 import CompanyReferenceType2


T = TypeVar("T", bound="ProfileCompanyInterestsData")


@_attrs_define
class ProfileCompanyInterestsData:
    """
    Attributes:
        company_interests (list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2]):
    """

    company_interests: list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2]

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415

        company_interests = []
        for componentsschemas_company_interest_list_item_data in self.company_interests:
            componentsschemas_company_interest_list_item: dict[str, Any]
            if isinstance(componentsschemas_company_interest_list_item_data, CompanyReferenceType0):
                componentsschemas_company_interest_list_item = (
                    componentsschemas_company_interest_list_item_data.to_dict()
                )
            elif isinstance(componentsschemas_company_interest_list_item_data, CompanyReferenceType1):
                componentsschemas_company_interest_list_item = (
                    componentsschemas_company_interest_list_item_data.to_dict()
                )
            else:
                componentsschemas_company_interest_list_item = (
                    componentsschemas_company_interest_list_item_data.to_dict()
                )

            company_interests.append(componentsschemas_company_interest_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "companyInterests": company_interests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.company_reference_type_2 import CompanyReferenceType2  # noqa: PLC0415

        d = dict(src_dict)
        company_interests = []
        _company_interests = d.pop("companyInterests")
        for componentsschemas_company_interest_list_item_data in _company_interests:

            def _parse_componentsschemas_company_interest_list_item(
                data: object,
            ) -> CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2:
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
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_reference_type_2 = CompanyReferenceType2.from_dict(data)

                return componentsschemas_company_reference_type_2

            componentsschemas_company_interest_list_item = _parse_componentsschemas_company_interest_list_item(
                componentsschemas_company_interest_list_item_data
            )

            company_interests.append(componentsschemas_company_interest_list_item)

        profile_company_interests_data = cls(
            company_interests=company_interests,
        )

        return profile_company_interests_data
