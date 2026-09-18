from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_job_search_query_experience import LinkedInV2JobSearchQueryExperience
from ..models.linked_in_v2_job_search_query_sort import LinkedInV2JobSearchQuerySort
from ..models.linked_in_v2_job_search_query_time_posted import LinkedInV2JobSearchQueryTimePosted
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2JobSearchQuery")


@_attrs_define
class LinkedInV2JobSearchQuery:
    """
    Attributes:
        keywords (str):
        start (int):  Default: 0.
        sort (LinkedInV2JobSearchQuerySort):  Default: LinkedInV2JobSearchQuerySort.RELEVANCE.
        time_posted (LinkedInV2JobSearchQueryTimePosted):  Default: LinkedInV2JobSearchQueryTimePosted.ANY.
        location (str | Unset): A location name or an ID from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`).
        company_slug (str | Unset):
        experience (LinkedInV2JobSearchQueryExperience | Unset):
    """

    keywords: str
    start: int = 0
    sort: LinkedInV2JobSearchQuerySort = LinkedInV2JobSearchQuerySort.RELEVANCE
    time_posted: LinkedInV2JobSearchQueryTimePosted = LinkedInV2JobSearchQueryTimePosted.ANY
    location: str | Unset = UNSET
    company_slug: str | Unset = UNSET
    experience: LinkedInV2JobSearchQueryExperience | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        start = self.start

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
                "start": start,
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

        start = d.pop("start")

        sort = LinkedInV2JobSearchQuerySort(d.pop("sort"))

        time_posted = LinkedInV2JobSearchQueryTimePosted(d.pop("timePosted"))

        location = d.pop("location", UNSET)

        company_slug = d.pop("companySlug", UNSET)

        _experience = d.pop("experience", UNSET)
        experience: LinkedInV2JobSearchQueryExperience | Unset
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = LinkedInV2JobSearchQueryExperience(_experience)

        linked_in_v2_job_search_query = cls(
            keywords=keywords,
            start=start,
            sort=sort,
            time_posted=time_posted,
            location=location,
            company_slug=company_slug,
            experience=experience,
        )

        return linked_in_v2_job_search_query
