from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.failed_section_meta import FailedSectionMeta
    from ..models.product_section_meta_type_0_type_0 import ProductSectionMetaType0Type0
    from ..models.product_section_meta_type_0_type_1 import ProductSectionMetaType0Type1
    from ..models.product_section_meta_type_1 import ProductSectionMetaType1
    from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0
    from ..models.required_core_section_meta_type_1 import RequiredCoreSectionMetaType1
    from ..models.skipped_section_meta import SkippedSectionMeta


T = TypeVar("T", bound="CompanySections")


@_attrs_define
class CompanySections:
    """
    Attributes:
        company (RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1):
        products (FailedSectionMeta | ProductSectionMetaType0Type0 | ProductSectionMetaType0Type1 |
            ProductSectionMetaType1 | SkippedSectionMeta):
    """

    company: RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1
    products: (
        FailedSectionMeta
        | ProductSectionMetaType0Type0
        | ProductSectionMetaType0Type1
        | ProductSectionMetaType1
        | SkippedSectionMeta
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.failed_section_meta import FailedSectionMeta  # noqa: PLC0415
        from ..models.product_section_meta_type_0_type_0 import ProductSectionMetaType0Type0  # noqa: PLC0415
        from ..models.product_section_meta_type_0_type_1 import ProductSectionMetaType0Type1  # noqa: PLC0415
        from ..models.product_section_meta_type_1 import ProductSectionMetaType1  # noqa: PLC0415
        from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0  # noqa: PLC0415

        company: dict[str, Any]
        if isinstance(self.company, RequiredCoreSectionMetaType0):
            company = self.company.to_dict()
        else:
            company = self.company.to_dict()

        products: dict[str, Any]
        if isinstance(self.products, ProductSectionMetaType0Type0):
            products = self.products.to_dict()
        elif isinstance(self.products, ProductSectionMetaType0Type1):
            products = self.products.to_dict()
        elif isinstance(self.products, ProductSectionMetaType1):
            products = self.products.to_dict()
        elif isinstance(self.products, FailedSectionMeta):
            products = self.products.to_dict()
        else:
            products = self.products.to_dict()

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
        from ..models.failed_section_meta import FailedSectionMeta  # noqa: PLC0415
        from ..models.product_section_meta_type_0_type_0 import ProductSectionMetaType0Type0  # noqa: PLC0415
        from ..models.product_section_meta_type_0_type_1 import ProductSectionMetaType0Type1  # noqa: PLC0415
        from ..models.product_section_meta_type_1 import ProductSectionMetaType1  # noqa: PLC0415
        from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0  # noqa: PLC0415
        from ..models.required_core_section_meta_type_1 import RequiredCoreSectionMetaType1  # noqa: PLC0415
        from ..models.skipped_section_meta import SkippedSectionMeta  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_company(data: object) -> RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_required_core_section_meta_type_0 = RequiredCoreSectionMetaType0.from_dict(data)

                return componentsschemas_required_core_section_meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_required_core_section_meta_type_1 = RequiredCoreSectionMetaType1.from_dict(data)

            return componentsschemas_required_core_section_meta_type_1

        company = _parse_company(d.pop("company"))

        def _parse_products(
            data: object,
        ) -> (
            FailedSectionMeta
            | ProductSectionMetaType0Type0
            | ProductSectionMetaType0Type1
            | ProductSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_product_section_meta_type_0_type_0 = ProductSectionMetaType0Type0.from_dict(data)

                return componentsschemas_product_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_product_section_meta_type_0_type_1 = ProductSectionMetaType0Type1.from_dict(data)

                return componentsschemas_product_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_product_section_meta_type_1 = ProductSectionMetaType1.from_dict(data)

                return componentsschemas_product_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_product_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_product_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_product_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_product_section_meta_type_3

        products = _parse_products(d.pop("products"))

        company_sections = cls(
            company=company,
            products=products,
        )

        return company_sections
