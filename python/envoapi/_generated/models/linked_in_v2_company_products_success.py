from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_products_data import CompanyProductsData
    from ..models.linked_in_v2_company_products_success_meta import LinkedInV2CompanyProductsSuccessMeta


T = TypeVar("T", bound="LinkedInV2CompanyProductsSuccess")


@_attrs_define
class LinkedInV2CompanyProductsSuccess:
    """
    Attributes:
        data (CompanyProductsData):
        meta (LinkedInV2CompanyProductsSuccessMeta):
    """

    data: CompanyProductsData
    meta: LinkedInV2CompanyProductsSuccessMeta

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_products_data import CompanyProductsData  # noqa: PLC0415
        from ..models.linked_in_v2_company_products_success_meta import (
            LinkedInV2CompanyProductsSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = CompanyProductsData.from_dict(d.pop("data"))

        meta = LinkedInV2CompanyProductsSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_company_products_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_company_products_success
