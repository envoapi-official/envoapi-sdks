from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IndustrySearchIndustry")


@_attrs_define
class IndustrySearchIndustry:
    """
    Attributes:
        id (str):
        label (str):
    """

    id: str
    label: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")
        if not isinstance(id, str):
            raise TypeError("Expected string for id")

        label = d.pop("label")
        if not isinstance(label, str):
            raise TypeError("Expected string for label")

        industry_search_industry = cls(
            id=id,
            label=label,
        )

        return industry_search_industry
