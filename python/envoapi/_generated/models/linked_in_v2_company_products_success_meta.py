from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_feature_paging import LinkedInV2FeaturePaging


T = TypeVar("T", bound="LinkedInV2CompanyProductsSuccessMeta")


@_attrs_define
class LinkedInV2CompanyProductsSuccessMeta:
    """
    Attributes:
        paging (LinkedInV2FeaturePaging):
        credit_cost (int):
    """

    paging: LinkedInV2FeaturePaging
    credit_cost: int

    def to_dict(self) -> dict[str, Any]:
        paging = self.paging.to_dict()

        credit_cost = self.credit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "paging": paging,
                "creditCost": credit_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_in_v2_feature_paging import LinkedInV2FeaturePaging  # noqa: PLC0415

        d = dict(src_dict)
        paging = LinkedInV2FeaturePaging.from_dict(d.pop("paging"))

        credit_cost = d.pop("creditCost")

        linked_in_v2_company_products_success_meta = cls(
            paging=paging,
            credit_cost=credit_cost,
        )

        return linked_in_v2_company_products_success_meta
