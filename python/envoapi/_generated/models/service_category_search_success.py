from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.service_category_search_data import ServiceCategorySearchData
    from ..models.service_category_search_success_meta import ServiceCategorySearchSuccessMeta


T = TypeVar("T", bound="ServiceCategorySearchSuccess")


@_attrs_define
class ServiceCategorySearchSuccess:
    """
    Attributes:
        data (ServiceCategorySearchData):
        meta (ServiceCategorySearchSuccessMeta):
    """

    data: ServiceCategorySearchData
    meta: ServiceCategorySearchSuccessMeta

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
        from ..models.service_category_search_data import ServiceCategorySearchData  # noqa: PLC0415
        from ..models.service_category_search_success_meta import ServiceCategorySearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ServiceCategorySearchData.from_dict(d.pop("data"))

        meta = ServiceCategorySearchSuccessMeta.from_dict(d.pop("meta"))

        service_category_search_success = cls(
            data=data,
            meta=meta,
        )

        return service_category_search_success
