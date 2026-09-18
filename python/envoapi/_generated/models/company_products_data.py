from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_product import CompanyProduct


T = TypeVar("T", bound="CompanyProductsData")


@_attrs_define
class CompanyProductsData:
    """
    Attributes:
        products (list[CompanyProduct]):
    """

    products: list[CompanyProduct]

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_product import CompanyProduct  # noqa: PLC0415

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = CompanyProduct.from_dict(products_item_data)

            products.append(products_item)

        company_products_data = cls(
            products=products,
        )

        return company_products_data
