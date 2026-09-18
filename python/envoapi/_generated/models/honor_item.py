from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.partial_date_type_0 import PartialDateType0
    from ..models.partial_date_type_1 import PartialDateType1


T = TypeVar("T", bound="HonorItem")


@_attrs_define
class HonorItem:
    """
    Attributes:
        title (str):
        issuer_name (None | str):
        issued_on (None | PartialDateType0 | PartialDateType1):
        description (None | str):
    """

    title: str
    issuer_name: None | str
    issued_on: None | PartialDateType0 | PartialDateType1
    description: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415

        title = self.title

        issuer_name: None | str
        issuer_name = self.issuer_name

        issued_on: dict[str, Any] | None
        if isinstance(self.issued_on, PartialDateType0):
            issued_on = self.issued_on.to_dict()
        elif isinstance(self.issued_on, PartialDateType1):
            issued_on = self.issued_on.to_dict()
        else:
            issued_on = self.issued_on

        description: None | str
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "issuerName": issuer_name,
                "issuedOn": issued_on,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")
        if not isinstance(title, str):
            raise TypeError("Expected string for title")

        def _parse_issuer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issuer_name = _parse_issuer_name(d.pop("issuerName"))

        def _parse_issued_on(data: object) -> None | PartialDateType0 | PartialDateType1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_0 = PartialDateType0.from_dict(data)

                return componentsschemas_partial_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_1 = PartialDateType1.from_dict(data)

                return componentsschemas_partial_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartialDateType0 | PartialDateType1, data)

        issued_on = _parse_issued_on(d.pop("issuedOn"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        honor_item = cls(
            title=title,
            issuer_name=issuer_name,
            issued_on=issued_on,
            description=description,
        )

        return honor_item
