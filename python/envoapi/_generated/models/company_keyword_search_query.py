from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyKeywordSearchQuery")


@_attrs_define
class CompanyKeywordSearchQuery:
    """
    Attributes:
        keywords (str):
        offset (int):  Default: 0.
        location (str | Unset): Up to 10 IDs from [Location search](../searchlocationsbykeyword/)
            (`data.locations[].id`), separated by commas. Matches any listed location, including branch offices. All other
            filters must also match.
        industry (str | Unset): Up to 10 IDs from [Industry search](../searchindustriesbykeyword/)
            (`data.industries[].id`), separated by commas. Matches any listed industry. All other filters must also match.
        company_size (str | Unset): Comma-separated employee-count buckets: B=1–10, C=11–50, D=51–200, E=201–500,
            F=501–1,000, G=1,001–5,000, H=5,001–10,000, I=10,001+. Use unique values; multiple buckets are OR.
        has_jobs (Literal['true'] | Unset): Set true to require job listings on LinkedIn. Omit for unrestricted results.
            false and 1 are not accepted; filtering for companies without jobs is not supported.
    """

    keywords: str
    offset: int = 0
    location: str | Unset = UNSET
    industry: str | Unset = UNSET
    company_size: str | Unset = UNSET
    has_jobs: Literal["true"] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        offset = self.offset

        location = self.location

        industry = self.industry

        company_size = self.company_size

        has_jobs = self.has_jobs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "offset": offset,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if industry is not UNSET:
            field_dict["industry"] = industry
        if company_size is not UNSET:
            field_dict["companySize"] = company_size
        if has_jobs is not UNSET:
            field_dict["hasJobs"] = has_jobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        offset = d.pop("offset")

        location = d.pop("location", UNSET)

        industry = d.pop("industry", UNSET)

        company_size = d.pop("companySize", UNSET)

        has_jobs = cast(Literal["true"] | Unset, d.pop("hasJobs", UNSET))
        if has_jobs != "true" and not isinstance(has_jobs, Unset):
            raise ValueError(f"hasJobs must match const 'true', got '{has_jobs}'")

        company_keyword_search_query = cls(
            keywords=keywords,
            offset=offset,
            location=location,
            industry=industry,
            company_size=company_size,
            has_jobs=has_jobs,
        )

        return company_keyword_search_query
