from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.resource_not_found_error import ResourceNotFoundError


T = TypeVar("T", bound="ResourceNotFoundErrorResponse")


@_attrs_define
class ResourceNotFoundErrorResponse:
    """
    Attributes:
        error (ResourceNotFoundError):
        meta (ErrorMetadata):
    """

    error: ResourceNotFoundError
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
        from ..models.resource_not_found_error import ResourceNotFoundError  # noqa: PLC0415

        d = dict(src_dict)
        error = ResourceNotFoundError.from_dict(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        resource_not_found_error_response = cls(
            error=error,
            meta=meta,
        )

        return resource_not_found_error_response
