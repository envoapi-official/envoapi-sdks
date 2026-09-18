from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyJobsCompany")


@_attrs_define
class CompanyJobsCompany:
    """
    Attributes:
        name (str):
        slug (str):
        url (str):
        logo_url (None | str):
    """

    name: str
    slug: str
    url: str
    logo_url: None | str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        url = self.url

        logo_url: None | str
        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "url": url,
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

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        company_jobs_company = cls(
            name=name,
            slug=slug,
            url=url,
            logo_url=logo_url,
        )

        return company_jobs_company
