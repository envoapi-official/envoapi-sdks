from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.search_posts_by_keyword_query_content_type import SearchPostsByKeywordQueryContentType
from ..models.search_posts_by_keyword_query_posted_within import SearchPostsByKeywordQueryPostedWithin
from ..models.search_posts_by_keyword_query_sort import SearchPostsByKeywordQuerySort
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPostsByKeywordQuery")


@_attrs_define
class SearchPostsByKeywordQuery:
    """
    Attributes:
        keywords (str):
        offset (int):  Default: 0.
        sort (SearchPostsByKeywordQuerySort):  Default: SearchPostsByKeywordQuerySort.RELEVANCE.
        posted_within (SearchPostsByKeywordQueryPostedWithin | Unset):
        content_type (SearchPostsByKeywordQueryContentType | Unset):
    """

    keywords: str
    offset: int = 0
    sort: SearchPostsByKeywordQuerySort = SearchPostsByKeywordQuerySort.RELEVANCE
    posted_within: SearchPostsByKeywordQueryPostedWithin | Unset = UNSET
    content_type: SearchPostsByKeywordQueryContentType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords

        offset = self.offset

        sort = self.sort.value

        posted_within: str | Unset = UNSET
        if not isinstance(self.posted_within, Unset):
            posted_within = self.posted_within.value

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keywords": keywords,
                "offset": offset,
                "sort": sort,
            }
        )
        if posted_within is not UNSET:
            field_dict["postedWithin"] = posted_within
        if content_type is not UNSET:
            field_dict["contentType"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = d.pop("keywords")
        if not isinstance(keywords, str):
            raise TypeError("Expected string for keywords")

        offset = d.pop("offset")

        sort = SearchPostsByKeywordQuerySort(d.pop("sort"))

        _posted_within = d.pop("postedWithin", UNSET)
        posted_within: SearchPostsByKeywordQueryPostedWithin | Unset
        if isinstance(_posted_within, Unset):
            posted_within = UNSET
        else:
            posted_within = SearchPostsByKeywordQueryPostedWithin(_posted_within)

        _content_type = d.pop("contentType", UNSET)
        content_type: SearchPostsByKeywordQueryContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = SearchPostsByKeywordQueryContentType(_content_type)

        search_posts_by_keyword_query = cls(
            keywords=keywords,
            offset=offset,
            sort=sort,
            posted_within=posted_within,
            content_type=content_type,
        )

        return search_posts_by_keyword_query
