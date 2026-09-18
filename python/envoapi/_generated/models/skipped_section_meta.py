from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.section_error import SectionError


T = TypeVar("T", bound="SkippedSectionMeta")


@_attrs_define
class SkippedSectionMeta:
    """
    Attributes:
        status (Literal['skipped']):
        returned_count (None):
        upstream_total (int | None):
        complete (None):
        truncated (None):
        next_cursor (None):
        error (None | SectionError):
    """

    status: Literal["skipped"]
    returned_count: None
    upstream_total: int | None
    complete: None
    truncated: None
    next_cursor: None
    error: None | SectionError

    def to_dict(self) -> dict[str, Any]:
        from ..models.section_error import SectionError  # noqa: PLC0415

        status = self.status

        returned_count = self.returned_count

        upstream_total: int | None
        upstream_total = self.upstream_total

        complete = self.complete

        truncated = self.truncated

        next_cursor = self.next_cursor

        error: dict[str, Any] | None
        if isinstance(self.error, SectionError):
            error = self.error.to_dict()
        else:
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
        from ..models.section_error import SectionError  # noqa: PLC0415

        d = dict(src_dict)
        status = cast(Literal["skipped"], d.pop("status"))
        if status != "skipped":
            raise ValueError(f"status must match const 'skipped', got '{status}'")

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

        def _parse_error(data: object) -> None | SectionError:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = SectionError.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SectionError, data)

        error = _parse_error(d.pop("error"))

        skipped_section_meta = cls(
            status=status,
            returned_count=returned_count,
            upstream_total=upstream_total,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
            error=error,
        )

        return skipped_section_meta
