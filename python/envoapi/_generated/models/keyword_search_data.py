from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.keyword_search_entity_type_0 import KeywordSearchEntityType0
    from ..models.keyword_search_entity_type_1 import KeywordSearchEntityType1
    from ..models.keyword_search_entity_type_2 import KeywordSearchEntityType2
    from ..models.keyword_search_entity_type_3 import KeywordSearchEntityType3
    from ..models.keyword_search_post import KeywordSearchPost


T = TypeVar("T", bound="KeywordSearchData")


@_attrs_define
class KeywordSearchData:
    """
    Attributes:
        results (list[KeywordSearchEntityType0 | KeywordSearchEntityType1 | KeywordSearchEntityType2 |
            KeywordSearchEntityType3 | KeywordSearchPost]):
    """

    results: list[
        KeywordSearchEntityType0
        | KeywordSearchEntityType1
        | KeywordSearchEntityType2
        | KeywordSearchEntityType3
        | KeywordSearchPost
    ]

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyword_search_entity_type_0 import KeywordSearchEntityType0  # noqa: PLC0415
        from ..models.keyword_search_entity_type_1 import KeywordSearchEntityType1  # noqa: PLC0415
        from ..models.keyword_search_entity_type_2 import KeywordSearchEntityType2  # noqa: PLC0415
        from ..models.keyword_search_entity_type_3 import KeywordSearchEntityType3  # noqa: PLC0415

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, KeywordSearchEntityType0):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, KeywordSearchEntityType1):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, KeywordSearchEntityType2):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, KeywordSearchEntityType3):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyword_search_entity_type_0 import KeywordSearchEntityType0  # noqa: PLC0415
        from ..models.keyword_search_entity_type_1 import KeywordSearchEntityType1  # noqa: PLC0415
        from ..models.keyword_search_entity_type_2 import KeywordSearchEntityType2  # noqa: PLC0415
        from ..models.keyword_search_entity_type_3 import KeywordSearchEntityType3  # noqa: PLC0415
        from ..models.keyword_search_post import KeywordSearchPost  # noqa: PLC0415

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> (
                KeywordSearchEntityType0
                | KeywordSearchEntityType1
                | KeywordSearchEntityType2
                | KeywordSearchEntityType3
                | KeywordSearchPost
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_keyword_search_entity_type_0 = KeywordSearchEntityType0.from_dict(data)

                    return componentsschemas_keyword_search_entity_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_keyword_search_entity_type_1 = KeywordSearchEntityType1.from_dict(data)

                    return componentsschemas_keyword_search_entity_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_keyword_search_entity_type_2 = KeywordSearchEntityType2.from_dict(data)

                    return componentsschemas_keyword_search_entity_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_keyword_search_entity_type_3 = KeywordSearchEntityType3.from_dict(data)

                    return componentsschemas_keyword_search_entity_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_keyword_search_item_type_1 = KeywordSearchPost.from_dict(data)

                return componentsschemas_keyword_search_item_type_1

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        keyword_search_data = cls(
            results=results,
        )

        return keyword_search_data
