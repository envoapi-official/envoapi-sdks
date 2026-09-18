from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.retryable_service_unavailable_error import RetryableServiceUnavailableError


T = TypeVar("T", bound="RetryableServiceUnavailableErrorResponse")


@_attrs_define
class RetryableServiceUnavailableErrorResponse:
    """
    Attributes:
        error (RetryableServiceUnavailableError):
        meta (ErrorMetadata):
    """

    error: RetryableServiceUnavailableError
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
        from ..models.retryable_service_unavailable_error import RetryableServiceUnavailableError  # noqa: PLC0415

        d = dict(src_dict)
        error = RetryableServiceUnavailableError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        retryable_service_unavailable_error_response = cls(
            error=error,
            meta=meta,
        )

        return retryable_service_unavailable_error_response
