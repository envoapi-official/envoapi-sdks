from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_job_filters_query_experience import LinkedInV2JobFiltersQueryExperience
from ..models.linked_in_v2_job_filters_query_sort import LinkedInV2JobFiltersQuerySort
from ..models.linked_in_v2_job_filters_query_time_posted import LinkedInV2JobFiltersQueryTimePosted
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2JobFiltersQuery")


@_attrs_define
class LinkedInV2JobFiltersQuery:
    """
    Attributes:
        keywords (str):
        sort (LinkedInV2JobFiltersQuerySort):  Default: LinkedInV2JobFiltersQuerySort.RELEVANCE.
        time_posted (LinkedInV2JobFiltersQueryTimePosted):  Default: LinkedInV2JobFiltersQueryTimePosted.ANY.
        location (str | Unset): A location name or an ID from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`).
        company_slug (str | Unset):
        experience (LinkedInV2JobFiltersQueryExperience | Unset):
    """

    keywords: str
    sort: LinkedInV2JobFiltersQuerySort = LinkedInV2JobFiltersQuerySort.RELEVANCE
    time_posted: LinkedInV2JobFiltersQueryTimePosted = LinkedInV2JobFiltersQueryTimePosted.ANY
    location: str | Unset = UNSET
    company_slug: str | Unset = UNSET
    experience: LinkedInV2JobFiltersQueryExperience | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        sort = self.sort.value

        time_posted = self.time_posted.value

        location = self.location

        company_slug = self.company_slug

        experience: str | Unset = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "sort": sort,
                "timePosted": time_posted,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if company_slug is not UNSET:
            field_dict["companySlug"] = company_slug
        if experience is not UNSET:
            field_dict["experience"] = experience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        sort = LinkedInV2JobFiltersQuerySort(d.pop("sort"))

        time_posted = LinkedInV2JobFiltersQueryTimePosted(d.pop("timePosted"))

        location = d.pop("location", UNSET)

        company_slug = d.pop("companySlug", UNSET)

        _experience = d.pop("experience", UNSET)
        experience: LinkedInV2JobFiltersQueryExperience | Unset
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = LinkedInV2JobFiltersQueryExperience(_experience)

        linked_in_v2_job_filters_query = cls(
            keywords=keywords,
            sort=sort,
            time_posted=time_posted,
            location=location,
            company_slug=company_slug,
            experience=experience,
        )

        return linked_in_v2_job_filters_query
