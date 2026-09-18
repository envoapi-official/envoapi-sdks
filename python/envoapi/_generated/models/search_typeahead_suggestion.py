from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_typeahead_suggestion_type import SearchTypeaheadSuggestionType

T = TypeVar("T", bound="SearchTypeaheadSuggestion")


@_attrs_define
class SearchTypeaheadSuggestion:
    """
    Attributes:
        text (str):
        description (None | str):
        type_ (SearchTypeaheadSuggestionType):
        url (str):
    """

    text: str
    description: None | str
    type_: SearchTypeaheadSuggestionType
    url: str

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        description: None | str
        description = self.description

        type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "description": description,
                "type": type_,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")
        if not isinstance(text, str):
            raise TypeError("Expected string for text")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        type_ = SearchTypeaheadSuggestionType(d.pop("type"))

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        search_typeahead_suggestion = cls(
            text=text,
            description=description,
            type_=type_,
            url=url,
        )

        return search_typeahead_suggestion
