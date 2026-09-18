from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_jobs_feed_query_experience import LinkedInV2JobsFeedQueryExperience
from ..models.linked_in_v2_jobs_feed_query_sort import LinkedInV2JobsFeedQuerySort
from ..models.linked_in_v2_jobs_feed_query_time_posted import LinkedInV2JobsFeedQueryTimePosted
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2JobsFeedQuery")


@_attrs_define
class LinkedInV2JobsFeedQuery:
    """
    Attributes:
        keywords (str):
        existing_results_count (int):  Default: 0.
        sort (LinkedInV2JobsFeedQuerySort):  Default: LinkedInV2JobsFeedQuerySort.RELEVANCE.
        time_posted (LinkedInV2JobsFeedQueryTimePosted):  Default: LinkedInV2JobsFeedQueryTimePosted.ANY.
        company_slug (str | Unset):
        experience (LinkedInV2JobsFeedQueryExperience | Unset):
        location (str | Unset): A location name or an ID from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`).
    """

    keywords: str
    existing_results_count: int = 0
    sort: LinkedInV2JobsFeedQuerySort = LinkedInV2JobsFeedQuerySort.RELEVANCE
    time_posted: LinkedInV2JobsFeedQueryTimePosted = LinkedInV2JobsFeedQueryTimePosted.ANY
    company_slug: str | Unset = UNSET
    experience: LinkedInV2JobsFeedQueryExperience | Unset = UNSET
    location: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        existing_results_count = self.existing_results_count

        sort = self.sort.value

        time_posted = self.time_posted.value

        company_slug = self.company_slug

        experience: str | Unset = UNSET
        if not isinstance(self.experience, Unset):
            experience = self.experience.value

        location = self.location

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "existingResultsCount": existing_results_count,
                "sort": sort,
                "timePosted": time_posted,
            }
        )
        if company_slug is not UNSET:
            field_dict["companySlug"] = company_slug
        if experience is not UNSET:
            field_dict["experience"] = experience
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        existing_results_count = d.pop("existingResultsCount")

        sort = LinkedInV2JobsFeedQuerySort(d.pop("sort"))

        time_posted = LinkedInV2JobsFeedQueryTimePosted(d.pop("timePosted"))

        company_slug = d.pop("companySlug", UNSET)

        _experience = d.pop("experience", UNSET)
        experience: LinkedInV2JobsFeedQueryExperience | Unset
        if isinstance(_experience, Unset):
            experience = UNSET
        else:
            experience = LinkedInV2JobsFeedQueryExperience(_experience)

        location = d.pop("location", UNSET)

        linked_in_v2_jobs_feed_query = cls(
            keywords=keywords,
            existing_results_count=existing_results_count,
            sort=sort,
            time_posted=time_posted,
            company_slug=company_slug,
            experience=experience,
            location=location,
        )

        return linked_in_v2_jobs_feed_query
