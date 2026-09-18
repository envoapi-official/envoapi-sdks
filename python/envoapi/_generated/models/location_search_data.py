from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.location_search_location import LocationSearchLocation


T = TypeVar("T", bound="LocationSearchData")


@_attrs_define
class LocationSearchData:
    """
    Attributes:
        locations (list[LocationSearchLocation]):
    """

    locations: list[LocationSearchLocation]

    def to_dict(self) -> dict[str, Any]:
        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()
            locations.append(locations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "locations": locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_search_location import LocationSearchLocation  # noqa: PLC0415

        d = dict(src_dict)
        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = LocationSearchLocation.from_dict(locations_item_data)

            locations.append(locations_item)

        location_search_data = cls(
            locations=locations,
        )

        return location_search_data
