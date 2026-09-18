from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.non_retryable_service_unavailable_error import NonRetryableServiceUnavailableError
    from ..models.retryable_service_unavailable_error import RetryableServiceUnavailableError


T = TypeVar("T", bound="ServiceUnavailableErrorResponse")


@_attrs_define
class ServiceUnavailableErrorResponse:
    """
    Attributes:
        error (NonRetryableServiceUnavailableError | RetryableServiceUnavailableError):
        meta (ErrorMetadata):
    """

    error: NonRetryableServiceUnavailableError | RetryableServiceUnavailableError
    meta: ErrorMetadata

    def to_dict(self) -> dict[str, Any]:
        from ..models.retryable_service_unavailable_error import RetryableServiceUnavailableError  # noqa: PLC0415

        error: dict[str, Any]
        if isinstance(self.error, RetryableServiceUnavailableError):
            error = self.error.to_dict()
        else:
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
        from ..models.retryable_service_unavailable_error import RetryableServiceUnavailableError  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_error(data: object) -> NonRetryableServiceUnavailableError | RetryableServiceUnavailableError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_service_unavailable_error_type_0 = RetryableServiceUnavailableError.from_dict(data)

                return componentsschemas_service_unavailable_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_service_unavailable_error_type_1 = NonRetryableServiceUnavailableError.from_dict(data)

            return componentsschemas_service_unavailable_error_type_1

        error = _parse_error(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        service_unavailable_error_response = cls(
            error=error,
            meta=meta,
        )

        return service_unavailable_error_response
