from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.section_error import SectionError


T = TypeVar("T", bound="FailedSectionMeta")


@_attrs_define
class FailedSectionMeta:
    """
    Attributes:
        status (Literal['failed']):
        returned_count (None):
        upstream_total (int | None):
        complete (None):
        truncated (None):
        next_cursor (None):
        error (SectionError):
    """

    status: Literal["failed"]
    returned_count: None
    upstream_total: int | None
    complete: None
    truncated: None
    next_cursor: None
    error: SectionError

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        returned_count = self.returned_count

        upstream_total: int | None
        upstream_total = self.upstream_total

        complete = self.complete

        truncated = self.truncated

        next_cursor = self.next_cursor

        error = self.error.to_dict()

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
        from ..models.section_error import SectionError  # noqa: PLC0415

        d = dict(src_dict)
        status = cast(Literal["failed"], d.pop("status"))
        if status != "failed":
            raise ValueError(f"status must match const 'failed', got '{status}'")

        returned_count = d.pop("returnedCount")
        if returned_count is not None:
            raise TypeError("Expected null for returned_count")

        def _parse_upstream_total(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        upstream_total = _parse_upstream_total(d.pop("upstreamTotal"))

        complete = d.pop("complete")
        if complete is not None:
            raise TypeError("Expected null for complete")

        truncated = d.pop("truncated")
        if truncated is not None:
            raise TypeError("Expected null for truncated")

        next_cursor = d.pop("nextCursor")
        if next_cursor is not None:
            raise TypeError("Expected null for next_cursor")

        error = SectionError.from_dict(d.pop("error"))

        failed_section_meta = cls(
            status=status,
            returned_count=returned_count,
            upstream_total=upstream_total,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
            error=error,
        )

        return failed_section_meta
