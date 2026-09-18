from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_post_author_kind import SearchPostAuthorKind

T = TypeVar("T", bound="SearchPostAuthor")


@_attrs_define
class SearchPostAuthor:
    """
    Attributes:
        kind (SearchPostAuthorKind):
        name (str):
        headline (None | str):
        url (str):
    """

    kind: SearchPostAuthorKind
    name: str
    headline: None | str
    url: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        headline: None | str
        headline = self.headline

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "headline": headline,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = SearchPostAuthorKind(d.pop("kind"))

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        search_post_author = cls(
            kind=kind,
            name=name,
            headline=headline,
            url=url,
        )

        return search_post_author
