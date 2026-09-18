from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyProduct")


@_attrs_define
class CompanyProduct:
    """
    Attributes:
        name (str):
        slug (None | str): Product slug, distinct from the owning Company slug.
        linkedin_url (None | str):
        description (None | str):
        is_signature_product (bool | None):
    """

    name: str
    slug: None | str
    linkedin_url: None | str
    description: None | str
    is_signature_product: bool | None

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | str
        slug = self.slug

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        description: None | str
        description = self.description

        is_signature_product: bool | None
        is_signature_product = self.is_signature_product

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "linkedinUrl": linkedin_url,
                "description": description,
                "isSignatureProduct": is_signature_product,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_is_signature_product(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_signature_product = _parse_is_signature_product(d.pop("isSignatureProduct"))

        company_product = cls(
            name=name,
            slug=slug,
            linkedin_url=linkedin_url,
            description=description,
            is_signature_product=is_signature_product,
        )

        return company_product
