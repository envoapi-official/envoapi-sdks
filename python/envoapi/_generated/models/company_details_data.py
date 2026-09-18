from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_location import CompanyLocation
    from ..models.employee_count_range import EmployeeCountRange
    from ..models.image_variant import ImageVariant
    from ..models.industry_reference_type_0 import IndustryReferenceType0
    from ..models.industry_reference_type_1 import IndustryReferenceType1
    from ..models.industry_reference_type_2 import IndustryReferenceType2
    from ..models.organization_type import OrganizationType
    from ..models.partial_date_type_0 import PartialDateType0
    from ..models.partial_date_type_1 import PartialDateType1
    from ..models.product_item import ProductItem


T = TypeVar("T", bound="CompanyDetailsData")


@_attrs_define
class CompanyDetailsData:
    """
    Attributes:
        public_id (str):
        name (None | str):
        slug (None | str):
        linkedin_url (None | str):
        website_url (None | str):
        description (None | str):
        tagline (None | str):
        founded_on (None | PartialDateType0 | PartialDateType1):
        organization_type (None | OrganizationType):
        specialties (list[str] | None):
        primary_industry (IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None):
        industries (list[IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2] | None):
        employee_count (int | None):
        employee_count_range (EmployeeCountRange | None):
        follower_count (int | None):
        logo (list[ImageVariant] | None):
        cover_image (list[ImageVariant] | None):
        headquarters (CompanyLocation | None):
        locations (list[CompanyLocation] | None):
        products (list[ProductItem] | None):
    """

    public_id: str
    name: None | str
    slug: None | str
    linkedin_url: None | str
    website_url: None | str
    description: None | str
    tagline: None | str
    founded_on: None | PartialDateType0 | PartialDateType1
    organization_type: None | OrganizationType
    specialties: list[str] | None
    primary_industry: IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None
    industries: list[IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2] | None
    employee_count: int | None
    employee_count_range: EmployeeCountRange | None
    follower_count: int | None
    logo: list[ImageVariant] | None
    cover_image: list[ImageVariant] | None
    headquarters: CompanyLocation | None
    locations: list[CompanyLocation] | None
    products: list[ProductItem] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_location import CompanyLocation  # noqa: PLC0415
        from ..models.employee_count_range import EmployeeCountRange  # noqa: PLC0415
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.organization_type import OrganizationType  # noqa: PLC0415
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415

        public_id = self.public_id

        name: None | str
        name = self.name

        slug: None | str
        slug = self.slug

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        website_url: None | str
        website_url = self.website_url

        description: None | str
        description = self.description

        tagline: None | str
        tagline = self.tagline

        founded_on: dict[str, Any] | None
        if isinstance(self.founded_on, PartialDateType0):
            founded_on = self.founded_on.to_dict()
        elif isinstance(self.founded_on, PartialDateType1):
            founded_on = self.founded_on.to_dict()
        else:
            founded_on = self.founded_on

        organization_type: dict[str, Any] | None
        if isinstance(self.organization_type, OrganizationType):
            organization_type = self.organization_type.to_dict()
        else:
            organization_type = self.organization_type

        specialties: list[str] | None
        if isinstance(self.specialties, list):
            specialties = self.specialties

        else:
            specialties = self.specialties

        primary_industry: dict[str, Any] | None
        if isinstance(self.primary_industry, IndustryReferenceType0):
            primary_industry = self.primary_industry.to_dict()
        elif isinstance(self.primary_industry, IndustryReferenceType1):
            primary_industry = self.primary_industry.to_dict()
        elif isinstance(self.primary_industry, IndustryReferenceType2):
            primary_industry = self.primary_industry.to_dict()
        else:
            primary_industry = self.primary_industry

        industries: list[dict[str, Any]] | None
        if isinstance(self.industries, list):
            industries = []
            for industries_type_0_item_data in self.industries:
                industries_type_0_item: dict[str, Any]
                if isinstance(industries_type_0_item_data, IndustryReferenceType0):
                    industries_type_0_item = industries_type_0_item_data.to_dict()
                elif isinstance(industries_type_0_item_data, IndustryReferenceType1):
                    industries_type_0_item = industries_type_0_item_data.to_dict()
                else:
                    industries_type_0_item = industries_type_0_item_data.to_dict()

                industries.append(industries_type_0_item)

        else:
            industries = self.industries

        employee_count: int | None
        employee_count = self.employee_count

        employee_count_range: dict[str, Any] | None
        if isinstance(self.employee_count_range, EmployeeCountRange):
            employee_count_range = self.employee_count_range.to_dict()
        else:
            employee_count_range = self.employee_count_range

        follower_count: int | None
        follower_count = self.follower_count

        logo: list[dict[str, Any]] | None
        if isinstance(self.logo, list):
            logo = []
            for componentsschemas_image_variant_list_item_data in self.logo:
                componentsschemas_image_variant_list_item = componentsschemas_image_variant_list_item_data.to_dict()
                logo.append(componentsschemas_image_variant_list_item)

        else:
            logo = self.logo

        cover_image: list[dict[str, Any]] | None
        if isinstance(self.cover_image, list):
            cover_image = []
            for componentsschemas_image_variant_list_item_data in self.cover_image:
                componentsschemas_image_variant_list_item = componentsschemas_image_variant_list_item_data.to_dict()
                cover_image.append(componentsschemas_image_variant_list_item)

        else:
            cover_image = self.cover_image

        headquarters: dict[str, Any] | None
        if isinstance(self.headquarters, CompanyLocation):
            headquarters = self.headquarters.to_dict()
        else:
            headquarters = self.headquarters

        locations: list[dict[str, Any]] | None
        if isinstance(self.locations, list):
            locations = []
            for locations_type_0_item_data in self.locations:
                locations_type_0_item = locations_type_0_item_data.to_dict()
                locations.append(locations_type_0_item)

        else:
            locations = self.locations

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
                "publicId": public_id,
                "name": name,
                "slug": slug,
                "linkedinUrl": linkedin_url,
                "websiteUrl": website_url,
                "description": description,
                "tagline": tagline,
                "foundedOn": founded_on,
                "organizationType": organization_type,
                "specialties": specialties,
                "primaryIndustry": primary_industry,
                "industries": industries,
                "employeeCount": employee_count,
                "employeeCountRange": employee_count_range,
                "followerCount": follower_count,
                "logo": logo,
                "coverImage": cover_image,
                "headquarters": headquarters,
                "locations": locations,
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_location import CompanyLocation  # noqa: PLC0415
        from ..models.employee_count_range import EmployeeCountRange  # noqa: PLC0415
        from ..models.image_variant import ImageVariant  # noqa: PLC0415
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.organization_type import OrganizationType  # noqa: PLC0415
        from ..models.partial_date_type_0 import PartialDateType0  # noqa: PLC0415
        from ..models.partial_date_type_1 import PartialDateType1  # noqa: PLC0415
        from ..models.product_item import ProductItem  # noqa: PLC0415

        d = dict(src_dict)
        public_id = d.pop("publicId")
        if not isinstance(public_id, str):
            raise TypeError("Expected string for public_id")

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

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("websiteUrl"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_tagline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tagline = _parse_tagline(d.pop("tagline"))

        def _parse_founded_on(data: object) -> None | PartialDateType0 | PartialDateType1:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_0 = PartialDateType0.from_dict(data)

                return componentsschemas_partial_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_partial_date_type_1 = PartialDateType1.from_dict(data)

                return componentsschemas_partial_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartialDateType0 | PartialDateType1, data)

        founded_on = _parse_founded_on(d.pop("foundedOn"))

        def _parse_organization_type(data: object) -> None | OrganizationType:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_type_0 = OrganizationType.from_dict(data)

                return organization_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationType, data)

        organization_type = _parse_organization_type(d.pop("organizationType"))

        def _parse_specialties(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specialties_type_0 = cast(list[str], data)

                return specialties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        specialties = _parse_specialties(d.pop("specialties"))

        def _parse_primary_industry(
            data: object,
        ) -> IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_industry_reference_type_0 = IndustryReferenceType0.from_dict(data)

                return componentsschemas_industry_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_industry_reference_type_1 = IndustryReferenceType1.from_dict(data)

                return componentsschemas_industry_reference_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_industry_reference_type_2 = IndustryReferenceType2.from_dict(data)

                return componentsschemas_industry_reference_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None, data)

        primary_industry = _parse_primary_industry(d.pop("primaryIndustry"))

        def _parse_industries(
            data: object,
        ) -> list[IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                industries_type_0 = []
                _industries_type_0 = data
                for industries_type_0_item_data in _industries_type_0:

                    def _parse_industries_type_0_item(
                        data: object,
                    ) -> IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_industry_reference_type_0 = IndustryReferenceType0.from_dict(data)

                            return componentsschemas_industry_reference_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_industry_reference_type_1 = IndustryReferenceType1.from_dict(data)

                            return componentsschemas_industry_reference_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_industry_reference_type_2 = IndustryReferenceType2.from_dict(data)

                        return componentsschemas_industry_reference_type_2

                    industries_type_0_item = _parse_industries_type_0_item(industries_type_0_item_data)

                    industries_type_0.append(industries_type_0_item)

                return industries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2] | None, data)

        industries = _parse_industries(d.pop("industries"))

        def _parse_employee_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        employee_count = _parse_employee_count(d.pop("employeeCount"))

        def _parse_employee_count_range(data: object) -> EmployeeCountRange | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                employee_count_range_type_0 = EmployeeCountRange.from_dict(data)

                return employee_count_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmployeeCountRange | None, data)

        employee_count_range = _parse_employee_count_range(d.pop("employeeCountRange"))

        def _parse_follower_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        follower_count = _parse_follower_count(d.pop("followerCount"))

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

        def _parse_cover_image(data: object) -> list[ImageVariant] | None:
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

        cover_image = _parse_cover_image(d.pop("coverImage"))

        def _parse_headquarters(data: object) -> CompanyLocation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headquarters_type_0 = CompanyLocation.from_dict(data)

                return headquarters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyLocation | None, data)

        headquarters = _parse_headquarters(d.pop("headquarters"))

        def _parse_locations(data: object) -> list[CompanyLocation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                locations_type_0 = []
                _locations_type_0 = data
                for locations_type_0_item_data in _locations_type_0:
                    locations_type_0_item = CompanyLocation.from_dict(locations_type_0_item_data)

                    locations_type_0.append(locations_type_0_item)

                return locations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyLocation] | None, data)

        locations = _parse_locations(d.pop("locations"))

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

        company_details_data = cls(
            public_id=public_id,
            name=name,
            slug=slug,
            linkedin_url=linkedin_url,
            website_url=website_url,
            description=description,
            tagline=tagline,
            founded_on=founded_on,
            organization_type=organization_type,
            specialties=specialties,
            primary_industry=primary_industry,
            industries=industries,
            employee_count=employee_count,
            employee_count_range=employee_count_range,
            follower_count=follower_count,
            logo=logo,
            cover_image=cover_image,
            headquarters=headquarters,
            locations=locations,
            products=products,
        )

        return company_details_data
