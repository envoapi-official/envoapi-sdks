from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_public_item_attributes_item_type_0_name import LinkedInV2PublicItemAttributesItemType0Name

T = TypeVar("T", bound="LinkedInV2PublicItemAttributesItemType0")


@_attrs_define
class LinkedInV2PublicItemAttributesItemType0:
    """
    Attributes:
        name (LinkedInV2PublicItemAttributesItemType0Name):
        value (str):
    """

    name: LinkedInV2PublicItemAttributesItemType0Name
    value: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = LinkedInV2PublicItemAttributesItemType0Name(d.pop("name"))

        value = d.pop("value")
        if not isinstance(value, str):
            raise TypeError("Expected string for value")

        linked_in_v2_public_item_attributes_item_type_0 = cls(
            name=name,
            value=value,
        )

        return linked_in_v2_public_item_attributes_item_type_0
