from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyInterestSectionMetaType0Type0Type0")


@_attrs_define
class CompanyInterestSectionMetaType0Type0Type0:
    """
    Attributes:
        status (Literal['complete']):
        returned_count (int):
        upstream_total (int | None):
        complete (bool):
        truncated (bool):
        next_cursor (None):
        error (None):
    """

    status: Literal["complete"]
    returned_count: int
    upstream_total: int | None
    complete: bool
    truncated: bool
    next_cursor: None
    error: None

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        returned_count = self.returned_count

        upstream_total: int | None
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

        company_interest_section_meta_type_0_type_0_type_0 = cls(
            status=status,
            returned_count=returned_count,
            upstream_total=upstream_total,
            complete=complete,
            truncated=truncated,
            next_cursor=next_cursor,
            error=error,
        )

        return company_interest_section_meta_type_0_type_0_type_0
