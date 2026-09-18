from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.product_item import ProductItem


T = TypeVar("T", bound="CompanyData")


@_attrs_define
class CompanyData:
    """
    Attributes:
        company (Company):
        products (list[ProductItem] | None):
    """

    company: Company
    products: list[ProductItem] | None

    def to_dict(self) -> dict[str, Any]:
        company = self.company.to_dict()

        products: list[dict[str, Any]] | None
        if isinstance(self.products, list):
            products = []
            for products_type_0_item_data in self.products:
                products_type_0_item = products_type_0_item_data.to_dict()
                products.append(products_type_0_item)

        else:
            products = self.products

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company": company,
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company  # noqa: PLC0415
        from ..models.product_item import ProductItem  # noqa: PLC0415

        d = dict(src_dict)
        company = Company.from_dict(d.pop("company"))

        def _parse_products(data: object) -> list[ProductItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                products_type_0 = []
                _products_type_0 = data
                for products_type_0_item_data in _products_type_0:
                    products_type_0_item = ProductItem.from_dict(products_type_0_item_data)

                    products_type_0.append(products_type_0_item)

                return products_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductItem] | None, data)

        products = _parse_products(d.pop("products"))

        company_data = cls(
            company=company,
            products=products,
        )

        return company_data
