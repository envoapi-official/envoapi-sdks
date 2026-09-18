from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LocationSearchLocation")


@_attrs_define
class LocationSearchLocation:
    """
    Attributes:
        id (str): Permanent Envo-owned location identifier. The underlying provider value is private.
        name (str):
    """

    id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")
        if not isinstance(id, str):
            raise TypeError("Expected string for id")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        location_search_location = cls(
            id=id,
            name=name,
        )

        return location_search_location
