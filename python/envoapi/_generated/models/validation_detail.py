from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.validation_detail_code import ValidationDetailCode

T = TypeVar("T", bound="ValidationDetail")


@_attrs_define
class ValidationDetail:
    """
    Attributes:
        field (str):
        code (ValidationDetailCode):
        message (str):
    """

    field: str
    code: ValidationDetailCode
    message: str

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        code = self.code.value

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field": field,
                "code": code,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")
        if not isinstance(field, str):
            raise TypeError("Expected string for field")

        code = ValidationDetailCode(d.pop("code"))

        message = d.pop("message")
        if not isinstance(message, str):
            raise TypeError("Expected string for message")

        validation_detail = cls(
            field=field,
            code=code,
            message=message,
        )

        return validation_detail
