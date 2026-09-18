from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetCompanyDetailsBySlugQuery")


@_attrs_define
class GetCompanyDetailsBySlugQuery:
    """
    Attributes:
        slug (str):
    """

    slug: str

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        get_company_details_by_slug_query = cls(
            slug=slug,
        )

        return get_company_details_by_slug_query
