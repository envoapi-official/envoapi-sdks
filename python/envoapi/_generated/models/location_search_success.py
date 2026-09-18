from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.location_search_data import LocationSearchData
    from ..models.location_search_success_meta import LocationSearchSuccessMeta


T = TypeVar("T", bound="LocationSearchSuccess")


@_attrs_define
class LocationSearchSuccess:
    """
    Attributes:
        data (LocationSearchData):
        meta (LocationSearchSuccessMeta):
    """

    data: LocationSearchData
    meta: LocationSearchSuccessMeta

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_search_data import LocationSearchData  # noqa: PLC0415
        from ..models.location_search_success_meta import LocationSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = LocationSearchData.from_dict(d.pop("data"))

        meta = LocationSearchSuccessMeta.from_dict(d.pop("meta"))

        location_search_success = cls(
            data=data,
            meta=meta,
        )

        return location_search_success
