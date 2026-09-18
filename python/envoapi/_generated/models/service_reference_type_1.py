from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServiceReferenceType1")


@_attrs_define
class ServiceReferenceType1:
    """
    Attributes:
        public_id (None):
        name (str):
    """

    public_id: None
    name: str

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_id = d.pop("publicId")
        if public_id is not None:
            raise TypeError("Expected null for public_id")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        service_reference_type_1 = cls(
            public_id=public_id,
            name=name,
        )

        return service_reference_type_1
