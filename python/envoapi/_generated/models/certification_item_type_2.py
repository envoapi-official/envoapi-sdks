from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CertificationItemType2")


@_attrs_define
class CertificationItemType2:
    """
    Attributes:
        expires_on (None):
        does_not_expire (None):
    """

    expires_on: None
    does_not_expire: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_on = self.expires_on

        does_not_expire = self.does_not_expire

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresOn": expires_on,
                "doesNotExpire": does_not_expire,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_on = d.pop("expiresOn")
        if expires_on is not None:
            raise TypeError("Expected null for expires_on")

        does_not_expire = d.pop("doesNotExpire")
        if does_not_expire is not None:
            raise TypeError("Expected null for does_not_expire")

        certification_item_type_2 = cls(
            expires_on=expires_on,
            does_not_expire=does_not_expire,
        )

        certification_item_type_2.additional_properties = d
        return certification_item_type_2

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
