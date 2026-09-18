from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SkillReferenceType0")


@_attrs_define
class SkillReferenceType0:
    """
    Attributes:
        public_id (str):
        name (None):
    """

    public_id: str
    name: None

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
        if not isinstance(public_id, str):
            raise TypeError("Expected string for public_id")

        name = d.pop("name")
        if name is not None:
            raise TypeError("Expected null for name")

        skill_reference_type_0 = cls(
            public_id=public_id,
            name=name,
        )

        return skill_reference_type_0
