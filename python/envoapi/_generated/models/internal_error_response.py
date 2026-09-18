from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.internal_error import InternalError


T = TypeVar("T", bound="InternalErrorResponse")


@_attrs_define
class InternalErrorResponse:
    """
    Attributes:
        error (InternalError):
        meta (ErrorMetadata):
    """

    error: InternalError
    meta: ErrorMetadata

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "error": error,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_metadata import ErrorMetadata  # noqa: PLC0415
        from ..models.internal_error import InternalError  # noqa: PLC0415

        d = dict(src_dict)
        error = InternalError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        internal_error_response = cls(
            error=error,
            meta=meta,
        )

        return internal_error_response
