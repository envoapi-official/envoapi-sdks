from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contact_phone_type import ContactPhoneType

T = TypeVar("T", bound="ContactPhone")


@_attrs_define
class ContactPhone:
    """
    Attributes:
        number (str):
        type_ (ContactPhoneType | None):
    """

    number: str
    type_: ContactPhoneType | None

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_: None | str
        if isinstance(self.type_, ContactPhoneType):
            type_ = self.type_.value
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "number": number,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")
        if not isinstance(number, str):
            raise TypeError("Expected string for number")

        def _parse_type_(data: object) -> ContactPhoneType | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = ContactPhoneType(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactPhoneType | None, data)

        type_ = _parse_type_(d.pop("type"))

        contact_phone = cls(
            number=number,
            type_=type_,
        )

        return contact_phone
