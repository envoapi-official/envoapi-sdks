from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_search_filters_query_result_type import LinkedInV2SearchFiltersQueryResultType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2SearchFiltersQuery")


@_attrs_define
class LinkedInV2SearchFiltersQuery:
    """
    Attributes:
        result_type (LinkedInV2SearchFiltersQueryResultType):
        keywords (str | Unset):
        current_company_slug (str | Unset):
        location (str | Unset): A location name or an ID from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`).
    """

    result_type: LinkedInV2SearchFiltersQueryResultType
    keywords: str | Unset = UNSET
    current_company_slug: str | Unset = UNSET
    location: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result_type = self.result_type.value

        keywords = self.keywords

        current_company_slug = self.current_company_slug

        location = self.location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resultType": result_type,
            }
        )
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if current_company_slug is not UNSET:
            field_dict["currentCompanySlug"] = current_company_slug
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result_type = LinkedInV2SearchFiltersQueryResultType(d.pop("resultType"))

        keywords = d.pop("keywords", UNSET)

        current_company_slug = d.pop("currentCompanySlug", UNSET)

        location = d.pop("location", UNSET)

        linked_in_v2_search_filters_query = cls(
            result_type=result_type,
            keywords=keywords,
            current_company_slug=current_company_slug,
            location=location,
        )

        return linked_in_v2_search_filters_query
