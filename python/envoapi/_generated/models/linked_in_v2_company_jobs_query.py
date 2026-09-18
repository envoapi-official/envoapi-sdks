from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LinkedInV2CompanyJobsQuery")


@_attrs_define
class LinkedInV2CompanyJobsQuery:
    """
    Attributes:
        slug (str):
        start (int): Zero-based offset into the first 1,000 matching jobs. Follow meta.paging.nextStart for subsequent
            pages. Default: 0.
    """

    slug: str
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
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

        start = d.pop("start")

        linked_in_v2_company_jobs_query = cls(
            slug=slug,
            start=start,
        )

        return linked_in_v2_company_jobs_query
