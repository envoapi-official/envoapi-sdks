from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostReactionsPaging")


@_attrs_define
class PostReactionsPaging:
    """
    Attributes:
        start (Literal[0]):
        count (int):
        has_more (bool):
    """

    start: Literal[0]
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
        start = cast(Literal[0], d.pop("start"))
        if start != 0:
            raise ValueError(f"start must match const 0, got '{start}'")

        count = d.pop("count")

        has_more = d.pop("hasMore")

        post_reactions_paging = cls(
            start=start,
            count=count,
            has_more=has_more,
        )

        return post_reactions_paging
