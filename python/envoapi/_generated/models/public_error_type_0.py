from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.public_error_type_0_code import PublicErrorType0Code

if TYPE_CHECKING:
    from ..models.validation_detail import ValidationDetail


T = TypeVar("T", bound="PublicErrorType0")


@_attrs_define
class PublicErrorType0:
    """
    Attributes:
        code (PublicErrorType0Code):
        message (str):
        retryable (bool):
        details (list[ValidationDetail]):
    """

    code: PublicErrorType0Code
    message: str
    retryable: bool
    details: list[ValidationDetail]

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

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
        code = PublicErrorType0Code(d.pop("code"))

        message = d.pop("message")
        if not isinstance(message, str):
            raise TypeError("Expected string for message")

        retryable = d.pop("retryable")

        details = []
        _details = d.pop("details")
        for details_item_data in _details:
            details_item = ValidationDetail.from_dict(details_item_data)

            details.append(details_item)

        public_error_type_0 = cls(
            code=code,
            message=message,
            retryable=retryable,
            details=details,
        )

        return public_error_type_0
