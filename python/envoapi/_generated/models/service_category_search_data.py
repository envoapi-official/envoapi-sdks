from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.service_category_search_item import ServiceCategorySearchItem


T = TypeVar("T", bound="ServiceCategorySearchData")


@_attrs_define
class ServiceCategorySearchData:
    """
    Attributes:
        service_categories (list[ServiceCategorySearchItem]):
    """

    service_categories: list[ServiceCategorySearchItem]

    def to_dict(self) -> dict[str, Any]:
        service_categories = []
        for service_categories_item_data in self.service_categories:
            service_categories_item = service_categories_item_data.to_dict()
            service_categories.append(service_categories_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceCategories": service_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_category_search_item import ServiceCategorySearchItem  # noqa: PLC0415

        d = dict(src_dict)
        service_categories = []
        _service_categories = d.pop("serviceCategories")
        for service_categories_item_data in _service_categories:
            service_categories_item = ServiceCategorySearchItem.from_dict(service_categories_item_data)

            service_categories.append(service_categories_item)

        service_category_search_data = cls(
            service_categories=service_categories,
        )

        return service_category_search_data
