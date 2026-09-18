from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SkillSectionMetaType0")


@_attrs_define
class SkillSectionMetaType0:
    """
    Attributes:
        status (Literal['complete']):
        returned_count (int):
        upstream_total (int | None):
        complete (bool):
        truncated (bool):
        next_cursor (None):
        error (None):
        has_more (bool | None | Unset):
    """

    status: Literal["complete"]
    returned_count: int
    upstream_total: int | None
    complete: bool
    truncated: bool
    next_cursor: None
    error: None
    has_more: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        returned_count = self.returned_count

        upstream_total: int | None
        upstream_total = self.upstream_total

        complete = self.complete

        truncated = self.truncated

        next_cursor = self.next_cursor

        error = self.error

        has_more: bool | None | Unset
        if isinstance(self.has_more, Unset):
            has_more = UNSET
        else:
            has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "returnedCount": returned_count,
                "upstreamTotal": upstream_total,
                "complete": complete,
                "truncated": truncated,
                "nextCursor": next_cursor,
                "error": error,
            }
        )
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal["complete"], d.pop("status"))
        if status != "complete":
            raise ValueError(f"status must match const 'complete', got '{status}'")

        returned_count = d.pop("returnedCount")

        def _parse_upstream_total(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        upstream_total = _parse_upstream_total(d.pop("upstreamTotal"))

        complete = d.pop("complete")

        truncated = d.pop("truncated")

        next_cursor = d.pop("nextCursor")
        if next_cursor is not None:
            raise TypeError("Expected null for next_cursor")

        error = d.pop("error")
        if error is not None:
            raise TypeError("Expected null for error")

        def _parse_has_more(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_more = _parse_has_more(d.pop("hasMore", UNSET))

        skill_section_meta_type_0 = cls(
            status=status,
            returned_count=returned_count,
            upstream_total=upstream_total,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
            error=error,
            has_more=has_more,
        )

        return skill_section_meta_type_0
