from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LinkedInV2EmptyQuery")


@_attrs_define
class LinkedInV2EmptyQuery:
    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        linked_in_v2_empty_query = cls()

        return linked_in_v2_empty_query
