from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ErrorMetadata")


@_attrs_define
class ErrorMetadata:
    """
    Attributes:
        request_id (str):
    """

    request_id: str

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requestId": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_id = d.pop("requestId")
        if not isinstance(request_id, str):
            raise TypeError("Expected string for request_id")

        error_metadata = cls(
            request_id=request_id,
        )

        return error_metadata
