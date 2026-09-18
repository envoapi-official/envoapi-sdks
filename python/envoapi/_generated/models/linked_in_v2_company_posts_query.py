from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.company_posts_filter import CompanyPostsFilter
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedInV2CompanyPostsQuery")


@_attrs_define
class LinkedInV2CompanyPostsQuery:
    """
    Attributes:
        slug (str):
        filter_ (CompanyPostsFilter):
        start (int): Initial offset. With a cursor, omit start or supply its next offset; the cursor determines
            continuation. Default: 0.
        cursor (str | Unset): Stateless Envo continuation cursor. Reuse with the same account, company and filter; use
            it before expiry. The backend fixes the page size.
    """

    slug: str
    filter_: CompanyPostsFilter
    start: int = 0
    cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        filter_ = self.filter_.value

        start = self.start

        cursor = self.cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "slug": slug,
                "filter": filter_,
                "start": start,
            }
        )
        if cursor is not UNSET:
            field_dict["cursor"] = cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        filter_ = CompanyPostsFilter(d.pop("filter"))

        start = d.pop("start")

        cursor = d.pop("cursor", UNSET)

        linked_in_v2_company_posts_query = cls(
            slug=slug,
            filter_=filter_,
            start=start,
            cursor=cursor,
        )

        return linked_in_v2_company_posts_query
