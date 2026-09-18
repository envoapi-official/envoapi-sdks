from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="EntityReferenceType2")


@_attrs_define
class EntityReferenceType2:
    """
    Attributes:
        public_id (str):
        name (str):
    """

    public_id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        public_id: str
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

        def _parse_public_id(data: object) -> str:
            return cast(str, data)

        public_id = _parse_public_id(d.pop("publicId"))

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        entity_reference_type_2 = cls(
            public_id=public_id,
            name=name,
        )

        return entity_reference_type_2
