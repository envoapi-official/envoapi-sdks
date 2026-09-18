from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.invalid_api_key_error import InvalidApiKeyError


T = TypeVar("T", bound="InvalidApiKeyErrorResponse")


@_attrs_define
class InvalidApiKeyErrorResponse:
    """
    Attributes:
        error (InvalidApiKeyError):
        meta (ErrorMetadata):
    """

    error: InvalidApiKeyError
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
        from ..models.invalid_api_key_error import InvalidApiKeyError  # noqa: PLC0415

        d = dict(src_dict)
        error = InvalidApiKeyError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        invalid_api_key_error_response = cls(
            error=error,
            meta=meta,
        )

        return invalid_api_key_error_response
