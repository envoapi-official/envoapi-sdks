from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LinkedInV2SimilarCompaniesQueryType0")


@_attrs_define
class LinkedInV2SimilarCompaniesQueryType0:
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

        linked_in_v2_similar_companies_query_type_0 = cls(
            slug=slug,
        )

        return linked_in_v2_similar_companies_query_type_0
