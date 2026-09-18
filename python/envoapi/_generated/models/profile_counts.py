from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileCounts")


@_attrs_define
class ProfileCounts:
    """
    Attributes:
        follower_count (int | None):
        connection_count (int | None):
    """

    follower_count: int | None
    connection_count: int | None

    def to_dict(self) -> dict[str, Any]:
        follower_count: int | None
        follower_count = self.follower_count

        connection_count: int | None
        connection_count = self.connection_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "followerCount": follower_count,
                "connectionCount": connection_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_follower_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        follower_count = _parse_follower_count(d.pop("followerCount"))

        def _parse_connection_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        connection_count = _parse_connection_count(d.pop("connectionCount"))

        profile_counts = cls(
            follower_count=follower_count,
            connection_count=connection_count,
        )

        return profile_counts
