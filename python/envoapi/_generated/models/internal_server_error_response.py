from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.internal_error import InternalError
    from ..models.response_too_large_error import ResponseTooLargeError


T = TypeVar("T", bound="InternalServerErrorResponse")


@_attrs_define
class InternalServerErrorResponse:
    """
    Attributes:
        error (InternalError | ResponseTooLargeError):
        meta (ErrorMetadata):
    """

    error: InternalError | ResponseTooLargeError
    meta: ErrorMetadata

    def to_dict(self) -> dict[str, Any]:
        from ..models.internal_error import InternalError  # noqa: PLC0415

        error: dict[str, Any]
        if isinstance(self.error, InternalError):
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
        from ..models.internal_error import InternalError  # noqa: PLC0415
        from ..models.response_too_large_error import ResponseTooLargeError  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_error(data: object) -> InternalError | ResponseTooLargeError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = InternalError.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            error_type_1 = ResponseTooLargeError.from_dict(data)

            return error_type_1

        error = _parse_error(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        internal_server_error_response = cls(
            error=error,
            meta=meta,
        )

        return internal_server_error_response
