from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.non_retryable_service_unavailable_error import NonRetryableServiceUnavailableError


T = TypeVar("T", bound="NonRetryableServiceUnavailableErrorResponse")


@_attrs_define
class NonRetryableServiceUnavailableErrorResponse:
    """
    Attributes:
        error (NonRetryableServiceUnavailableError):
        meta (ErrorMetadata):
    """

    error: NonRetryableServiceUnavailableError
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
        from ..models.non_retryable_service_unavailable_error import (
            NonRetryableServiceUnavailableError,  # noqa: PLC0415
        )

        d = dict(src_dict)
        error = NonRetryableServiceUnavailableError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        non_retryable_service_unavailable_error_response = cls(
            error=error,
            meta=meta,
        )

        return non_retryable_service_unavailable_error_response
