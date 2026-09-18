from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LookupAuthenticationHeaders")


@_attrs_define
class LookupAuthenticationHeaders:
    """
    Attributes:
        authorization (str):
    """

    authorization: str

    def to_dict(self) -> dict[str, Any]:
        authorization = self.authorization

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authorization": authorization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authorization = d.pop("authorization")
        if not isinstance(authorization, str):
            raise TypeError("Expected string for authorization")

        lookup_authentication_headers = cls(
            authorization=authorization,
        )

        return lookup_authentication_headers
