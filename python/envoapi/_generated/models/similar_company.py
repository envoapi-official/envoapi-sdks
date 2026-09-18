from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimilarCompany")


@_attrs_define
class SimilarCompany:
    """
    Attributes:
        slug (str):
        company_url (str):
        name (str):
        industry (str):
        logo_url (None | str):
    """

    slug: str
    company_url: str
    name: str
    industry: str
    logo_url: None | str

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        company_url = self.company_url

        name = self.name

        industry = self.industry

        logo_url: None | str
        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "companyUrl": company_url,
                "name": name,
                "industry": industry,
                "logoUrl": logo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        company_url = d.pop("companyUrl")
        if not isinstance(company_url, str):
            raise TypeError("Expected string for company_url")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        industry = d.pop("industry")
        if not isinstance(industry, str):
            raise TypeError("Expected string for industry")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        similar_company = cls(
            slug=slug,
            company_url=company_url,
            name=name,
            industry=industry,
            logo_url=logo_url,
        )

        return similar_company
