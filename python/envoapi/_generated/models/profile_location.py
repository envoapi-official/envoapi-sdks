from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileLocation")


@_attrs_define
class ProfileLocation:
    """
    Attributes:
        display_name (None | str):
        locality (None | str):
        country (None | str):
        country_code (None | str):
    """

    display_name: None | str
    locality: None | str
    country: None | str
    country_code: None | str

    def to_dict(self) -> dict[str, Any]:
        display_name: None | str
        display_name = self.display_name

        locality: None | str
        locality = self.locality

        country: None | str
        country = self.country

        country_code: None | str
        country_code = self.country_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "displayName": display_name,
                "locality": locality,
                "country": country,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))

        def _parse_locality(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locality = _parse_locality(d.pop("locality"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("countryCode"))

        profile_location = cls(
            display_name=display_name,
            locality=locality,
            country=country,
            country_code=country_code,
        )

        return profile_location
