from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_domain_search_company import CompanyDomainSearchCompany


T = TypeVar("T", bound="CompanyDomainSearchData")


@_attrs_define
class CompanyDomainSearchData:
    """
    Attributes:
        companies (list[CompanyDomainSearchCompany]):
    """

    companies: list[CompanyDomainSearchCompany]

    def to_dict(self) -> dict[str, Any]:
        companies = []
        for companies_item_data in self.companies:
            companies_item = companies_item_data.to_dict()
            companies.append(companies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "companies": companies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_domain_search_company import CompanyDomainSearchCompany  # noqa: PLC0415

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = CompanyDomainSearchCompany.from_dict(companies_item_data)

            companies.append(companies_item)

        company_domain_search_data = cls(
            companies=companies,
        )

        return company_domain_search_data
