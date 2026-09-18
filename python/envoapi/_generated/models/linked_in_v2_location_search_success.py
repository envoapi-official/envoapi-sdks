from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_location_search_success_meta import LinkedInV2LocationSearchSuccessMeta
    from ..models.location_search_data import LocationSearchData


T = TypeVar("T", bound="LinkedInV2LocationSearchSuccess")


@_attrs_define
class LinkedInV2LocationSearchSuccess:
    """
    Attributes:
        data (LocationSearchData):
        meta (LinkedInV2LocationSearchSuccessMeta):
    """

    data: LocationSearchData
    meta: LinkedInV2LocationSearchSuccessMeta

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
        from ..models.linked_in_v2_location_search_success_meta import (
            LinkedInV2LocationSearchSuccessMeta,  # noqa: PLC0415
        )
        from ..models.location_search_data import LocationSearchData  # noqa: PLC0415

        d = dict(src_dict)
        data = LocationSearchData.from_dict(d.pop("data"))

        meta = LinkedInV2LocationSearchSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_location_search_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_location_search_success
