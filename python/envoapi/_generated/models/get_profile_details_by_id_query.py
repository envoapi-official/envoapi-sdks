from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetProfileDetailsByIdQuery")


@_attrs_define
class GetProfileDetailsByIdQuery:
    """
    Attributes:
        public_id (str):
    """

    public_id: str

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_id = d.pop("publicId")
        if not isinstance(public_id, str):
            raise TypeError("Expected string for public_id")

        get_profile_details_by_id_query = cls(
            public_id=public_id,
        )

        return get_profile_details_by_id_query
