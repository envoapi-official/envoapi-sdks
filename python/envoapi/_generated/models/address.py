from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        line1 (None | str):
        line2 (None | str):
        locality (None | str):
        administrative_area (None | str):
        postal_code (None | str):
        country (None | str):
        country_code (None | str):
    """

    line1: None | str
    line2: None | str
    locality: None | str
    administrative_area: None | str
    postal_code: None | str
    country: None | str
    country_code: None | str

    def to_dict(self) -> dict[str, Any]:
        line1: None | str
        line1 = self.line1

        line2: None | str
        line2 = self.line2

        locality: None | str
        locality = self.locality

        administrative_area: None | str
        administrative_area = self.administrative_area

        postal_code: None | str
        postal_code = self.postal_code

        country: None | str
        country = self.country

        country_code: None | str
        country_code = self.country_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "line1": line1,
                "line2": line2,
                "locality": locality,
                "administrativeArea": administrative_area,
                "postalCode": postal_code,
                "country": country,
                "countryCode": country_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_line1(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line1 = _parse_line1(d.pop("line1"))

        def _parse_line2(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line2 = _parse_line2(d.pop("line2"))

        def _parse_locality(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locality = _parse_locality(d.pop("locality"))

        def _parse_administrative_area(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        administrative_area = _parse_administrative_area(d.pop("administrativeArea"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postalCode"))

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

        address = cls(
            line1=line1,
            line2=line2,
            locality=locality,
            administrative_area=administrative_area,
            postal_code=postal_code,
            country=country,
            country_code=country_code,
        )

        return address
