from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_activity_query_kind import LinkedInV2ActivityQueryKind

T = TypeVar("T", bound="LinkedInV2ActivityQuery")


@_attrs_define
class LinkedInV2ActivityQuery:
    """
    Attributes:
        username (str):
        kind (LinkedInV2ActivityQueryKind):
        start (int):  Default: 0.
    """

    username: str
    kind: LinkedInV2ActivityQueryKind
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        kind = self.kind.value

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "kind": kind,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        kind = LinkedInV2ActivityQueryKind(d.pop("kind"))

        start = d.pop("start")

        linked_in_v2_activity_query = cls(
            username=username,
            kind=kind,
            start=start,
        )

        return linked_in_v2_activity_query
