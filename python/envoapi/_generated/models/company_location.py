from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.address import Address


T = TypeVar("T", bound="CompanyLocation")


@_attrs_define
class CompanyLocation:
    """
    Attributes:
        description (None | str):
        address (Address | None):
    """

    description: None | str
    address: Address | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.address import Address  # noqa: PLC0415

        description: None | str
        description = self.description

        address: dict[str, Any] | None
        if isinstance(self.address, Address):
            address = self.address.to_dict()
        else:
            address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_address(data: object) -> Address | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = Address.from_dict(data)

                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Address | None, data)

        address = _parse_address(d.pop("address"))

        company_location = cls(
            description=description,
            address=address,
        )

        return company_location
