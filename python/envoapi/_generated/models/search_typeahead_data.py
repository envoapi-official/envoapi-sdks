from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_typeahead_suggestion import SearchTypeaheadSuggestion


T = TypeVar("T", bound="SearchTypeaheadData")


@_attrs_define
class SearchTypeaheadData:
    """
    Attributes:
        suggestions (list[SearchTypeaheadSuggestion]):
    """

    suggestions: list[SearchTypeaheadSuggestion]

    def to_dict(self) -> dict[str, Any]:
        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "suggestions": suggestions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_typeahead_suggestion import SearchTypeaheadSuggestion  # noqa: PLC0415

        d = dict(src_dict)
        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = SearchTypeaheadSuggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        search_typeahead_data = cls(
            suggestions=suggestions,
        )

        return search_typeahead_data
