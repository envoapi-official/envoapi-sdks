from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeywordSearchEntityType2")


@_attrs_define
class KeywordSearchEntityType2:
    """
    Attributes:
        kind (Literal['school']):
        name (str):
        description (None | str):
        additional_info (None | str):
        url (str):
    """

    kind: Literal["school"]
    name: str
    description: None | str
    additional_info: None | str
    url: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        name = self.name

        description: None | str
        description = self.description

        additional_info: None | str
        additional_info = self.additional_info

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "description": description,
                "additionalInfo": additional_info,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["school"], d.pop("kind"))
        if kind != "school":
            raise ValueError(f"kind must match const 'school', got '{kind}'")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_additional_info(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        additional_info = _parse_additional_info(d.pop("additionalInfo"))

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        keyword_search_entity_type_2 = cls(
            kind=kind,
            name=name,
            description=description,
            additional_info=additional_info,
            url=url,
        )

        return keyword_search_entity_type_2
