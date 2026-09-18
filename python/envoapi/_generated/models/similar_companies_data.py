from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.similar_company import SimilarCompany


T = TypeVar("T", bound="SimilarCompaniesData")


@_attrs_define
class SimilarCompaniesData:
    """
    Attributes:
        companies (list[SimilarCompany]):
    """

    companies: list[SimilarCompany]

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
        from ..models.similar_company import SimilarCompany  # noqa: PLC0415

        d = dict(src_dict)
        companies = []
        _companies = d.pop("companies")
        for companies_item_data in _companies:
            companies_item = SimilarCompany.from_dict(companies_item_data)

            companies.append(companies_item)

        similar_companies_data = cls(
            companies=companies,
        )

        return similar_companies_data
