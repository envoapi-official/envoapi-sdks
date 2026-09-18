from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NotRequestedSectionMeta")


@_attrs_define
class NotRequestedSectionMeta:
    """
    Attributes:
        status (Literal['notRequested']):
        returned_count (None):
        upstream_total (None):
        complete (None):
        truncated (None):
        next_cursor (None):
        error (None):
    """

    status: Literal["notRequested"]
    returned_count: None
    upstream_total: None
    complete: None
    truncated: None
    next_cursor: None
    error: None

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        returned_count = self.returned_count

        upstream_total = self.upstream_total

        complete = self.complete

        truncated = self.truncated

        next_cursor = self.next_cursor

        error = self.error

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal["notRequested"], d.pop("status"))
        if status != "notRequested":
            raise ValueError(f"status must match const 'notRequested', got '{status}'")

        returned_count = d.pop("returnedCount")
        if returned_count is not None:
            raise TypeError("Expected null for returned_count")

        upstream_total = d.pop("upstreamTotal")
        if upstream_total is not None:
            raise TypeError("Expected null for upstream_total")

        complete = d.pop("complete")
        if complete is not None:
            raise TypeError("Expected null for complete")

        truncated = d.pop("truncated")
        if truncated is not None:
            raise TypeError("Expected null for truncated")

        next_cursor = d.pop("nextCursor")
        if next_cursor is not None:
            raise TypeError("Expected null for next_cursor")

        error = d.pop("error")
        if error is not None:
            raise TypeError("Expected null for error")

        not_requested_section_meta = cls(
            status=status,
            returned_count=returned_count,
            upstream_total=upstream_total,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
            error=error,
        )

        return not_requested_section_meta
