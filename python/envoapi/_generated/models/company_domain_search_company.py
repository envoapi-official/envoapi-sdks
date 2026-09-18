from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyDomainSearchCompany")


@_attrs_define
class CompanyDomainSearchCompany:
    """
    Attributes:
        name (str):
        slug (str):
        linkedin_url (str):
        description (str):
        summary (None | str):
        logo_url (None | str):
    """

    name: str
    slug: str
    linkedin_url: str
    description: str
    summary: None | str
    logo_url: None | str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        linkedin_url = self.linkedin_url

        description = self.description

        summary: None | str
        summary = self.summary

        logo_url: None | str
        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "linkedinUrl": linkedin_url,
                "description": description,
                "summary": summary,
                "logoUrl": logo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        linkedin_url = d.pop("linkedinUrl")
        if not isinstance(linkedin_url, str):
            raise TypeError("Expected string for linkedin_url")

        description = d.pop("description")
        if not isinstance(description, str):
            raise TypeError("Expected string for description")

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        company_domain_search_company = cls(
            name=name,
            slug=slug,
            linkedin_url=linkedin_url,
            description=description,
            summary=summary,
            logo_url=logo_url,
        )

        return company_domain_search_company
