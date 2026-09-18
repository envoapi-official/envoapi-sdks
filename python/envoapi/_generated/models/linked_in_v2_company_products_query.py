from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_company_products_query_state import LinkedInV2CompanyProductsQueryState

T = TypeVar("T", bound="LinkedInV2CompanyProductsQuery")


@_attrs_define
class LinkedInV2CompanyProductsQuery:
    """
    Attributes:
        slug (str):
        state (LinkedInV2CompanyProductsQueryState):  Default: LinkedInV2CompanyProductsQueryState.PUBLISHED.
        start (int):  Default: 0.
    """

    slug: str
    state: LinkedInV2CompanyProductsQueryState = LinkedInV2CompanyProductsQueryState.PUBLISHED
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        state = self.state.value

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "state": state,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        state = LinkedInV2CompanyProductsQueryState(d.pop("state"))

        start = d.pop("start")

        linked_in_v2_company_products_query = cls(
            slug=slug,
            state=state,
            start=start,
        )

        return linked_in_v2_company_products_query
