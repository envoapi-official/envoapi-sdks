from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.validation_detail import ValidationDetail


T = TypeVar("T", bound="MethodNotAllowedError")


@_attrs_define
class MethodNotAllowedError:
    """
    Attributes:
        code (Literal['method_not_allowed']):
        message (str):
        retryable (bool):
        details (list[ValidationDetail]):
    """

    code: Literal["method_not_allowed"]
    message: str
    retryable: bool
    details: list[ValidationDetail]

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        retryable = self.retryable

        details = []
        for details_item_data in self.details:
            details_item = details_item_data.to_dict()
            details.append(details_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
                "retryable": retryable,
                "details": details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_detail import ValidationDetail  # noqa: PLC0415

        d = dict(src_dict)
        code = cast(Literal["method_not_allowed"], d.pop("code"))
        if code != "method_not_allowed":
            raise ValueError(f"code must match const 'method_not_allowed', got '{code}'")

        message = d.pop("message")
        if not isinstance(message, str):
            raise TypeError("Expected string for message")

        retryable = d.pop("retryable")

        details = []
        _details = d.pop("details")
        for details_item_data in _details:
            details_item = ValidationDetail.from_dict(details_item_data)

            details.append(details_item)

        method_not_allowed_error = cls(
            code=code,
            message=message,
            retryable=retryable,
            details=details,
        )

        return method_not_allowed_error
