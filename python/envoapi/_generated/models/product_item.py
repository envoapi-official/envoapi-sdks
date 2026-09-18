from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.category_reference_type_0 import CategoryReferenceType0
    from ..models.category_reference_type_1 import CategoryReferenceType1
    from ..models.category_reference_type_2 import CategoryReferenceType2
    from ..models.image_variant import ImageVariant
    from ..models.skill_reference_type_0 import SkillReferenceType0
    from ..models.skill_reference_type_1 import SkillReferenceType1
    from ..models.skill_reference_type_2 import SkillReferenceType2


T = TypeVar("T", bound="ProductItem")


@_attrs_define
class ProductItem:
    """
    Attributes:
        public_id (None | str):
        name (None | str):
        slug (None | str):
        description (None | str):
        is_signature_product (bool | None):
        logo (list[ImageVariant] | None):
        categories (list[CategoryReferenceType0 | CategoryReferenceType1 | CategoryReferenceType2] | None):
        skills (list[SkillReferenceType0 | SkillReferenceType1 | SkillReferenceType2] | None):
    """

    public_id: None | str
    name: None | str
    slug: None | str
    description: None | str
    is_signature_product: bool | None
    logo: list[ImageVariant] | None
    categories: list[CategoryReferenceType0 | CategoryReferenceType1 | CategoryReferenceType2] | None
    skills: list[SkillReferenceType0 | SkillReferenceType1 | SkillReferenceType2] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.category_reference_type_0 import CategoryReferenceType0  # noqa: PLC0415
        from ..models.category_reference_type_1 import CategoryReferenceType1  # noqa: PLC0415
        from ..models.skill_reference_type_0 import SkillReferenceType0  # noqa: PLC0415
        from ..models.skill_reference_type_1 import SkillReferenceType1  # noqa: PLC0415

        public_id: None | str
        public_id = self.public_id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        description: None | str
        description = self.description

        is_signature_product: bool | None
        is_signature_product = self.is_signature_product

        logo: list[dict[str, Any]] | None
        if isinstance(self.logo, list):
            logo = []
            for componentsschemas_image_variant_list_item_data in self.logo:
                componentsschemas_image_variant_list_item = componentsschemas_image_variant_list_item_data.to_dict()
                logo.append(componentsschemas_image_variant_list_item)

        else:
            logo = self.logo

        categories: list[dict[str, Any]] | None
        if isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item: dict[str, Any]
                if isinstance(categories_type_0_item_data, CategoryReferenceType0):
                    categories_type_0_item = categories_type_0_item_data.to_dict()
                elif isinstance(categories_type_0_item_data, CategoryReferenceType1):
                    categories_type_0_item = categories_type_0_item_data.to_dict()
                else:
                    categories_type_0_item = categories_type_0_item_data.to_dict()

                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        skills: list[dict[str, Any]] | None
        if isinstance(self.skills, list):
            skills = []
            for skills_type_0_item_data in self.skills:
                skills_type_0_item: dict[str, Any]
                if isinstance(skills_type_0_item_data, SkillReferenceType0):
                    skills_type_0_item = skills_type_0_item_data.to_dict()
                elif isinstance(skills_type_0_item_data, SkillReferenceType1):
                    skills_type_0_item = skills_type_0_item_data.to_dict()
                else:
                    skills_type_0_item = skills_type_0_item_data.to_dict()

                skills.append(skills_type_0_item)

        else:
            skills = self.skills

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
                "name": name,
                "slug": slug,
                "description": description,
                "isSignatureProduct": is_signature_product,
                "logo": logo,
                "categories": categories,
                "skills": skills,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_reference_type_0 import CategoryReferenceType0  # noqa: PLC0415
        from ..models.category_reference_type_1 import CategoryReferenceType1  # noqa: PLC0415
        from ..models.category_reference_type_2 import CategoryReferenceType2  # noqa: PLC0415
        from ..models.image_variant import ImageVariant  # noqa: PLC0415
        from ..models.skill_reference_type_0 import SkillReferenceType0  # noqa: PLC0415
        from ..models.skill_reference_type_1 import SkillReferenceType1  # noqa: PLC0415
        from ..models.skill_reference_type_2 import SkillReferenceType2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_public_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_id = _parse_public_id(d.pop("publicId"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_is_signature_product(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_signature_product = _parse_is_signature_product(d.pop("isSignatureProduct"))

        def _parse_logo(data: object) -> list[ImageVariant] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_image_slot_type_0 = []
                _componentsschemas_image_slot_type_0 = data
                for componentsschemas_image_variant_list_item_data in _componentsschemas_image_slot_type_0:
                    componentsschemas_image_variant_list_item = ImageVariant.from_dict(
                        componentsschemas_image_variant_list_item_data
                    )

                    componentsschemas_image_slot_type_0.append(componentsschemas_image_variant_list_item)

                return componentsschemas_image_slot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ImageVariant] | None, data)

        logo = _parse_logo(d.pop("logo"))

        def _parse_categories(
            data: object,
        ) -> list[CategoryReferenceType0 | CategoryReferenceType1 | CategoryReferenceType2] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:

                    def _parse_categories_type_0_item(
                        data: object,
                    ) -> CategoryReferenceType0 | CategoryReferenceType1 | CategoryReferenceType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_category_reference_type_0 = CategoryReferenceType0.from_dict(data)

                            return componentsschemas_category_reference_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_category_reference_type_1 = CategoryReferenceType1.from_dict(data)

                            return componentsschemas_category_reference_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_category_reference_type_2 = CategoryReferenceType2.from_dict(data)

                        return componentsschemas_category_reference_type_2

                    categories_type_0_item = _parse_categories_type_0_item(categories_type_0_item_data)

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CategoryReferenceType0 | CategoryReferenceType1 | CategoryReferenceType2] | None, data)

        categories = _parse_categories(d.pop("categories"))

        def _parse_skills(data: object) -> list[SkillReferenceType0 | SkillReferenceType1 | SkillReferenceType2] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = []
                _skills_type_0 = data
                for skills_type_0_item_data in _skills_type_0:

                    def _parse_skills_type_0_item(
                        data: object,
                    ) -> SkillReferenceType0 | SkillReferenceType1 | SkillReferenceType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_skill_reference_type_0 = SkillReferenceType0.from_dict(data)

                            return componentsschemas_skill_reference_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_skill_reference_type_1 = SkillReferenceType1.from_dict(data)

                            return componentsschemas_skill_reference_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_skill_reference_type_2 = SkillReferenceType2.from_dict(data)

                        return componentsschemas_skill_reference_type_2

                    skills_type_0_item = _parse_skills_type_0_item(skills_type_0_item_data)

                    skills_type_0.append(skills_type_0_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SkillReferenceType0 | SkillReferenceType1 | SkillReferenceType2] | None, data)

        skills = _parse_skills(d.pop("skills"))

        product_item = cls(
            public_id=public_id,
            name=name,
            slug=slug,
            description=description,
            is_signature_product=is_signature_product,
            logo=logo,
            categories=categories,
            skills=skills,
        )

        return product_item
