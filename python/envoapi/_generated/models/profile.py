from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.image_variant import ImageVariant
    from ..models.industry_reference_type_0 import IndustryReferenceType0
    from ..models.industry_reference_type_1 import IndustryReferenceType1
    from ..models.industry_reference_type_2 import IndustryReferenceType2
    from ..models.locale import Locale
    from ..models.profile_location import ProfileLocation


T = TypeVar("T", bound="Profile")


@_attrs_define
class Profile:
    """
    Attributes:
        public_id (str):
        username (None | str):
        linkedin_url (None | str):
        full_name (None | str):
        first_name (None | str):
        last_name (None | str):
        headline (None | str):
        about (None | str):
        profile_images (list[ImageVariant] | None):
        background_images (list[ImageVariant] | None):
        location (None | ProfileLocation):
        industry (IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None):
        primary_locale (Locale | None):
        supported_locales (list[Locale] | None):
        is_premium (bool | None):
        is_influencer (bool | None):
        is_creator (bool | None):
        is_open_to_work (bool | None): Whether the profile displays the public Open to Work frame. False means the frame
            is absent; null means the public frame status is unavailable. Does not expose recruiter-only preferences.
        is_hiring (bool | None): Whether the profile displays the public Hiring frame. False means the frame is absent;
            null means the public frame status is unavailable. Does not establish whether the person or company has open
            jobs.
        is_memorialized (bool | None):
    """

    public_id: str
    username: None | str
    linkedin_url: None | str
    full_name: None | str
    first_name: None | str
    last_name: None | str
    headline: None | str
    about: None | str
    profile_images: list[ImageVariant] | None
    background_images: list[ImageVariant] | None
    location: None | ProfileLocation
    industry: IndustryReferenceType0 | IndustryReferenceType1 | IndustryReferenceType2 | None
    primary_locale: Locale | None
    supported_locales: list[Locale] | None
    is_premium: bool | None
    is_influencer: bool | None
    is_creator: bool | None
    is_open_to_work: bool | None
    is_hiring: bool | None
    is_memorialized: bool | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.locale import Locale  # noqa: PLC0415
        from ..models.profile_location import ProfileLocation  # noqa: PLC0415

        public_id = self.public_id

        username: None | str
        username = self.username

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        full_name: None | str
        full_name = self.full_name

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        headline: None | str
        headline = self.headline

        about: None | str
        about = self.about

        profile_images: list[dict[str, Any]] | None
        if isinstance(self.profile_images, list):
            profile_images = []
            for componentsschemas_image_variant_list_item_data in self.profile_images:
                componentsschemas_image_variant_list_item = componentsschemas_image_variant_list_item_data.to_dict()
                profile_images.append(componentsschemas_image_variant_list_item)

        else:
            profile_images = self.profile_images

        background_images: list[dict[str, Any]] | None
        if isinstance(self.background_images, list):
            background_images = []
            for componentsschemas_image_variant_list_item_data in self.background_images:
                componentsschemas_image_variant_list_item = componentsschemas_image_variant_list_item_data.to_dict()
                background_images.append(componentsschemas_image_variant_list_item)

        else:
            background_images = self.background_images

        location: dict[str, Any] | None
        if isinstance(self.location, ProfileLocation):
            location = self.location.to_dict()
        else:
            location = self.location

        industry: dict[str, Any] | None
        if isinstance(self.industry, IndustryReferenceType0):
            industry = self.industry.to_dict()
        elif isinstance(self.industry, IndustryReferenceType1):
            industry = self.industry.to_dict()
        elif isinstance(self.industry, IndustryReferenceType2):
            industry = self.industry.to_dict()
        else:
            industry = self.industry

        primary_locale: dict[str, Any] | None
        if isinstance(self.primary_locale, Locale):
            primary_locale = self.primary_locale.to_dict()
        else:
            primary_locale = self.primary_locale

        supported_locales: list[dict[str, Any]] | None
        if isinstance(self.supported_locales, list):
            supported_locales = []
            for componentsschemas_supported_locale_list_item_data in self.supported_locales:
                componentsschemas_supported_locale_list_item = (
                    componentsschemas_supported_locale_list_item_data.to_dict()
                )
                supported_locales.append(componentsschemas_supported_locale_list_item)

        else:
            supported_locales = self.supported_locales

        is_premium: bool | None
        is_premium = self.is_premium

        is_influencer: bool | None
        is_influencer = self.is_influencer

        is_creator: bool | None
        is_creator = self.is_creator

        is_open_to_work: bool | None
        is_open_to_work = self.is_open_to_work

        is_hiring: bool | None
        is_hiring = self.is_hiring

        is_memorialized: bool | None
        is_memorialized = self.is_memorialized

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
                "username": username,
                "linkedinUrl": linkedin_url,
                "fullName": full_name,
                "firstName": first_name,
                "lastName": last_name,
                "headline": headline,
                "about": about,
                "profileImages": profile_images,
                "backgroundImages": background_images,
                "location": location,
                "industry": industry,
                "primaryLocale": primary_locale,
                "supportedLocales": supported_locales,
                "isPremium": is_premium,
                "isInfluencer": is_influencer,
                "isCreator": is_creator,
                "isOpenToWork": is_open_to_work,
                "isHiring": is_hiring,
                "isMemorialized": is_memorialized,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_variant import ImageVariant  # noqa: PLC0415
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.locale import Locale  # noqa: PLC0415
        from ..models.profile_location import ProfileLocation  # noqa: PLC0415

        d = dict(src_dict)
        public_id = d.pop("publicId")
        if not isinstance(public_id, str):
            raise TypeError("Expected string for public_id")

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(d.pop("username"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedinUrl"))

        def _parse_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_name = _parse_full_name(d.pop("fullName"))

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        def _parse_about(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        about = _parse_about(d.pop("about"))

        def _parse_profile_images(data: object) -> list[ImageVariant] | None:
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

        profile_images = _parse_profile_images(d.pop("profileImages"))

        def _parse_background_images(data: object) -> list[ImageVariant] | None:
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

        background_images = _parse_background_images(d.pop("backgroundImages"))

        def _parse_location(data: object) -> None | ProfileLocation:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = ProfileLocation.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileLocation, data)

        location = _parse_location(d.pop("location"))

        def _parse_industry(
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

        industry = _parse_industry(d.pop("industry"))

        def _parse_primary_locale(data: object) -> Locale | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_locale_type_0 = Locale.from_dict(data)

                return primary_locale_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Locale | None, data)

        primary_locale = _parse_primary_locale(d.pop("primaryLocale"))

        def _parse_supported_locales(data: object) -> list[Locale] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_supported_locales_type_0 = []
                _componentsschemas_supported_locales_type_0 = data
                for componentsschemas_supported_locale_list_item_data in _componentsschemas_supported_locales_type_0:
                    componentsschemas_supported_locale_list_item = Locale.from_dict(
                        componentsschemas_supported_locale_list_item_data
                    )

                    componentsschemas_supported_locales_type_0.append(componentsschemas_supported_locale_list_item)

                return componentsschemas_supported_locales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Locale] | None, data)

        supported_locales = _parse_supported_locales(d.pop("supportedLocales"))

        def _parse_is_premium(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_premium = _parse_is_premium(d.pop("isPremium"))

        def _parse_is_influencer(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_influencer = _parse_is_influencer(d.pop("isInfluencer"))

        def _parse_is_creator(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_creator = _parse_is_creator(d.pop("isCreator"))

        def _parse_is_open_to_work(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_open_to_work = _parse_is_open_to_work(d.pop("isOpenToWork"))

        def _parse_is_hiring(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_hiring = _parse_is_hiring(d.pop("isHiring"))

        def _parse_is_memorialized(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_memorialized = _parse_is_memorialized(d.pop("isMemorialized"))

        profile = cls(
            public_id=public_id,
            username=username,
            linkedin_url=linkedin_url,
            full_name=full_name,
            first_name=first_name,
            last_name=last_name,
            headline=headline,
            about=about,
            profile_images=profile_images,
            background_images=background_images,
            location=location,
            industry=industry,
            primary_locale=primary_locale,
            supported_locales=supported_locales,
            is_premium=is_premium,
            is_influencer=is_influencer,
            is_creator=is_creator,
            is_open_to_work=is_open_to_work,
            is_hiring=is_hiring,
            is_memorialized=is_memorialized,
        )

        return profile
