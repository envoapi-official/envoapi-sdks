from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.public_error_type_0 import PublicErrorType0
    from ..models.public_error_type_1 import PublicErrorType1
    from ..models.public_error_type_2 import PublicErrorType2


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """
    Attributes:
        error (PublicErrorType0 | PublicErrorType1 | PublicErrorType2):
        meta (ErrorMetadata):
    """

    error: PublicErrorType0 | PublicErrorType1 | PublicErrorType2
    meta: ErrorMetadata

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_error_type_0 import PublicErrorType0  # noqa: PLC0415
        from ..models.public_error_type_1 import PublicErrorType1  # noqa: PLC0415

        error: dict[str, Any]
        if isinstance(self.error, PublicErrorType0):
            error = self.error.to_dict()
        elif isinstance(self.error, PublicErrorType1):
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
        from ..models.public_error_type_0 import PublicErrorType0  # noqa: PLC0415
        from ..models.public_error_type_1 import PublicErrorType1  # noqa: PLC0415
        from ..models.public_error_type_2 import PublicErrorType2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_error(data: object) -> PublicErrorType0 | PublicErrorType1 | PublicErrorType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_public_error_type_0 = PublicErrorType0.from_dict(data)

                return componentsschemas_public_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_public_error_type_1 = PublicErrorType1.from_dict(data)

                return componentsschemas_public_error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_public_error_type_2 = PublicErrorType2.from_dict(data)

            return componentsschemas_public_error_type_2

        error = _parse_error(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        error_response = cls(
            error=error,
            meta=meta,
        )

        return error_response
