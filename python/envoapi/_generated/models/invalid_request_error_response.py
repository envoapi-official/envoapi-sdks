from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.invalid_request_error import InvalidRequestError


T = TypeVar("T", bound="InvalidRequestErrorResponse")


@_attrs_define
class InvalidRequestErrorResponse:
    """
    Attributes:
        error (InvalidRequestError):
        meta (ErrorMetadata):
    """

    error: InvalidRequestError
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
        from ..models.invalid_request_error import InvalidRequestError  # noqa: PLC0415

        d = dict(src_dict)
        error = InvalidRequestError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        invalid_request_error_response = cls(
            error=error,
            meta=meta,
        )

        return invalid_request_error_response
