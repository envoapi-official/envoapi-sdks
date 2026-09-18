from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeopleKeywordSearchQuery")


@_attrs_define
class PeopleKeywordSearchQuery:
    """
    Attributes:
        keywords (str):
        offset (int):  Default: 0.
        location (str | Unset): Location IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`). Separate IDs with commas.
        current_company (str | Unset): Current employer IDs from [Company details](../getcompanydetailsbyslug/)
            (`data.company.publicId`), separated by commas. Find company slugs with [Company
            search](../searchcompaniesbykeyword/).
        past_company (str | Unset): Past employer IDs from [Company details](../getcompanydetailsbyslug/)
            (`data.company.publicId`), separated by commas. Find company slugs with [Company
            search](../searchcompaniesbykeyword/).
        school_filter (str | Unset): School IDs from [School search](../searchschoolsbykeyword/) (`data.schools[].id`).
            Separate IDs with commas.
        profile_language (str | Unset): Comma-separated Profile language values: cs, da, de, en, es, fr, in, it, ja, ko,
            ms, nl, no, pl, pt, ro, ru, sv, tr, zh, _o. Use in for Indonesian, zh for Chinese, and _o for other profile
            languages.
        service_category (str | Unset): Category IDs from [Service category search](../searchservicecategories/)
            (`data.serviceCategories[].id`). Separate IDs with commas.
        industry (str | Unset): Industry IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`). Separate IDs with commas.
    """

    keywords: str
    offset: int = 0
    location: str | Unset = UNSET
    current_company: str | Unset = UNSET
    past_company: str | Unset = UNSET
    school_filter: str | Unset = UNSET
    profile_language: str | Unset = UNSET
    service_category: str | Unset = UNSET
    industry: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        offset = self.offset

        location = self.location

        current_company = self.current_company

        past_company = self.past_company

        school_filter = self.school_filter

        profile_language = self.profile_language

        service_category = self.service_category

        industry = self.industry

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "offset": offset,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if current_company is not UNSET:
            field_dict["currentCompany"] = current_company
        if past_company is not UNSET:
            field_dict["pastCompany"] = past_company
        if school_filter is not UNSET:
            field_dict["schoolFilter"] = school_filter
        if profile_language is not UNSET:
            field_dict["profileLanguage"] = profile_language
        if service_category is not UNSET:
            field_dict["serviceCategory"] = service_category
        if industry is not UNSET:
            field_dict["industry"] = industry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        offset = d.pop("offset")

        location = d.pop("location", UNSET)

        current_company = d.pop("currentCompany", UNSET)

        past_company = d.pop("pastCompany", UNSET)

        school_filter = d.pop("schoolFilter", UNSET)

        profile_language = d.pop("profileLanguage", UNSET)

        service_category = d.pop("serviceCategory", UNSET)

        industry = d.pop("industry", UNSET)

        people_keyword_search_query = cls(
            keywords=keywords,
            offset=offset,
            location=location,
            current_company=current_company,
            past_company=past_company,
            school_filter=school_filter,
            profile_language=profile_language,
            service_category=service_category,
            industry=industry,
        )

        return people_keyword_search_query
