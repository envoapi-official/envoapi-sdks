from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProfileCertificationItemType0")


@_attrs_define
class ProfileCertificationItemType0:
    """
    Attributes:
        does_not_expire (Literal[False]):
    """

    does_not_expire: Literal[False]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        does_not_expire = self.does_not_expire

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "doesNotExpire": does_not_expire,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        does_not_expire = cast(Literal[False], d.pop("doesNotExpire"))
        if does_not_expire != False:
            raise ValueError(f"doesNotExpire must match const False, got '{does_not_expire}'")

        profile_certification_item_type_0 = cls(
            does_not_expire=does_not_expire,
        )

        profile_certification_item_type_0.additional_properties = d
        return profile_certification_item_type_0

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
