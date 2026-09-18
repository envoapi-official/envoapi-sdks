from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileCompanyInterestsLookupQueryType2")


@_attrs_define
class ProfileCompanyInterestsLookupQueryType2:
    """
    Attributes:
        public_id (str):
        start (int):  Default: 0.
    """

    public_id: str
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_id = d.pop("publicId")
        if not isinstance(public_id, str):
            raise TypeError("Expected string for public_id")

        start = d.pop("start")

        profile_company_interests_lookup_query_type_2 = cls(
            public_id=public_id,
            start=start,
        )

        return profile_company_interests_lookup_query_type_2
