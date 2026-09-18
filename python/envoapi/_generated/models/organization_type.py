from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.organization_type_code import OrganizationTypeCode

T = TypeVar("T", bound="OrganizationType")


@_attrs_define
class OrganizationType:
    """
    Attributes:
        code (None | OrganizationTypeCode):
        name (None | str):
    """

    code: None | OrganizationTypeCode
    name: None | str

    def to_dict(self) -> dict[str, Any]:
        code: None | str
        if isinstance(self.code, OrganizationTypeCode):
            code = self.code.value
        else:
            code = self.code

        name: None | str
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_code(data: object) -> None | OrganizationTypeCode:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                code_type_0 = OrganizationTypeCode(data)

                return code_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationTypeCode, data)

        code = _parse_code(d.pop("code"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        organization_type = cls(
            code=code,
            name=name,
        )

        return organization_type
