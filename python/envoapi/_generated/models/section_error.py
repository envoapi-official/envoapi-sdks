from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.section_error_code import SectionErrorCode

T = TypeVar("T", bound="SectionError")


@_attrs_define
class SectionError:
    """
    Attributes:
        code (SectionErrorCode):
        message (str):
        retryable (bool):
    """

    code: SectionErrorCode
    message: str
    retryable: bool

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        retryable = self.retryable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
                "retryable": retryable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = SectionErrorCode(d.pop("code"))

        message = d.pop("message")
        if not isinstance(message, str):
            raise TypeError("Expected string for message")

        retryable = d.pop("retryable")

        section_error = cls(
            code=code,
            message=message,
            retryable=retryable,
        )

        return section_error
