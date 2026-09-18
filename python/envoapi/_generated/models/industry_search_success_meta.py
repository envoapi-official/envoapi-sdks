from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="IndustrySearchSuccessMeta")


@_attrs_define
class IndustrySearchSuccessMeta:
    """
    Attributes:
        credit_cost (int):
    """

    credit_cost: int

    def to_dict(self) -> dict[str, Any]:
        credit_cost = self.credit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "creditCost": credit_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit_cost = d.pop("creditCost")

        industry_search_success_meta = cls(
            credit_cost=credit_cost,
        )

        return industry_search_success_meta
