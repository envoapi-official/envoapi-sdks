from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_suspended_error import AccountSuspendedError
    from ..models.error_metadata import ErrorMetadata
    from ..models.insufficient_scope_error import InsufficientScopeError


T = TypeVar("T", bound="LookupForbiddenErrorResponse")


@_attrs_define
class LookupForbiddenErrorResponse:
    """
    Attributes:
        error (AccountSuspendedError | InsufficientScopeError):
        meta (ErrorMetadata):
    """

    error: AccountSuspendedError | InsufficientScopeError
    meta: ErrorMetadata

    def to_dict(self) -> dict[str, Any]:
        from ..models.insufficient_scope_error import InsufficientScopeError  # noqa: PLC0415

        error: dict[str, Any]
        if isinstance(self.error, InsufficientScopeError):
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
        from ..models.account_suspended_error import AccountSuspendedError  # noqa: PLC0415
        from ..models.error_metadata import ErrorMetadata  # noqa: PLC0415
        from ..models.insufficient_scope_error import InsufficientScopeError  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_error(data: object) -> AccountSuspendedError | InsufficientScopeError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = InsufficientScopeError.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            error_type_1 = AccountSuspendedError.from_dict(data)

            return error_type_1

        error = _parse_error(d.pop("error"))

        meta = ErrorMetadata.from_dict(d.pop("meta"))

        lookup_forbidden_error_response = cls(
            error=error,
            meta=meta,
        )

        return lookup_forbidden_error_response
