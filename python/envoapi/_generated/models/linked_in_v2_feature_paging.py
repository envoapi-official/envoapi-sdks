from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LinkedInV2FeaturePaging")


@_attrs_define
class LinkedInV2FeaturePaging:
    """
    Attributes:
        start (int):
        count (int):
        has_more (bool):
    """

    start: int
    count: int
    has_more: bool

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        count = self.count

        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start": start,
                "count": count,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        count = d.pop("count")

        has_more = d.pop("hasMore")

        linked_in_v2_feature_paging = cls(
            start=start,
            count=count,
            has_more=has_more,
        )

        return linked_in_v2_feature_paging
