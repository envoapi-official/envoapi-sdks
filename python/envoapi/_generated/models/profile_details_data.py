from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.course_item import CourseItem
    from ..models.education_item import EducationItem
    from ..models.honor_item import HonorItem
    from ..models.image_variant import ImageVariant
    from ..models.industry_reference_type_0 import IndustryReferenceType0
    from ..models.industry_reference_type_1 import IndustryReferenceType1
    from ..models.industry_reference_type_2 import IndustryReferenceType2
    from ..models.language_item import LanguageItem
    from ..models.locale import Locale
    from ..models.organization_membership_item import OrganizationMembershipItem
    from ..models.position_item import PositionItem
    from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0
    from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1
    from ..models.profile_counts import ProfileCounts
    from ..models.profile_location import ProfileLocation
    from ..models.volunteer_experience_item import VolunteerExperienceItem


T = TypeVar("T", bound="ProfileDetailsData")


@_attrs_define
class ProfileDetailsData:
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
        counts (None | ProfileCounts):
        experience (list[PositionItem] | None):
        education (list[EducationItem] | None):
        skills (list[str] | None): Skills preview; may contain only the first page. See meta.skills.hasMore and page
            through Get Profile Skills for the complete list.
        certifications (list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1] | None):
        organizations (list[OrganizationMembershipItem] | None):
        languages (list[LanguageItem] | None):
        courses (list[CourseItem] | None):
        volunteer_experience (list[VolunteerExperienceItem] | None):
        honors (list[HonorItem] | None):
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
    counts: None | ProfileCounts
    experience: list[PositionItem] | None
    education: list[EducationItem] | None
    skills: list[str] | None
    certifications: list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1] | None
    organizations: list[OrganizationMembershipItem] | None
    languages: list[LanguageItem] | None
    courses: list[CourseItem] | None
    volunteer_experience: list[VolunteerExperienceItem] | None
    honors: list[HonorItem] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.locale import Locale  # noqa: PLC0415
        from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0  # noqa: PLC0415
        from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1  # noqa: PLC0415
        from ..models.profile_counts import ProfileCounts  # noqa: PLC0415
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

        counts: dict[str, Any] | None
        if isinstance(self.counts, ProfileCounts):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        experience: list[dict[str, Any]] | None
        if isinstance(self.experience, list):
            experience = []
            for componentsschemas_position_list_item_data in self.experience:
                componentsschemas_position_list_item = componentsschemas_position_list_item_data.to_dict()
                experience.append(componentsschemas_position_list_item)

        else:
            experience = self.experience

        education: list[dict[str, Any]] | None
        if isinstance(self.education, list):
            education = []
            for componentsschemas_education_list_item_data in self.education:
                componentsschemas_education_list_item = componentsschemas_education_list_item_data.to_dict()
                education.append(componentsschemas_education_list_item)

        else:
            education = self.education

        skills: list[str] | None
        if isinstance(self.skills, list):
            skills = self.skills

        else:
            skills = self.skills

        certifications: list[Any | dict[str, Any]] | None
        if isinstance(self.certifications, list):
            certifications = []
            for componentsschemas_profile_certification_list_item_data in self.certifications:
                componentsschemas_profile_certification_list_item: Any | dict[str, Any]
                if isinstance(componentsschemas_profile_certification_list_item_data, ProfileCertificationItemType0):
                    componentsschemas_profile_certification_list_item = (
                        componentsschemas_profile_certification_list_item_data.to_dict()
                    )
                elif isinstance(componentsschemas_profile_certification_list_item_data, ProfileCertificationItemType1):
                    componentsschemas_profile_certification_list_item = (
                        componentsschemas_profile_certification_list_item_data.to_dict()
                    )
                else:
                    componentsschemas_profile_certification_list_item = (
                        componentsschemas_profile_certification_list_item_data
                    )
                certifications.append(componentsschemas_profile_certification_list_item)

        else:
            certifications = self.certifications

        organizations: list[dict[str, Any]] | None
        if isinstance(self.organizations, list):
            organizations = []
            for organizations_type_0_item_data in self.organizations:
                organizations_type_0_item = organizations_type_0_item_data.to_dict()
                organizations.append(organizations_type_0_item)

        else:
            organizations = self.organizations

        languages: list[dict[str, Any]] | None
        if isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item = languages_type_0_item_data.to_dict()
                languages.append(languages_type_0_item)

        else:
            languages = self.languages

        courses: list[dict[str, Any]] | None
        if isinstance(self.courses, list):
            courses = []
            for componentsschemas_course_list_item_data in self.courses:
                componentsschemas_course_list_item = componentsschemas_course_list_item_data.to_dict()
                courses.append(componentsschemas_course_list_item)

        else:
            courses = self.courses

        volunteer_experience: list[dict[str, Any]] | None
        if isinstance(self.volunteer_experience, list):
            volunteer_experience = []
            for componentsschemas_volunteer_experience_list_item_data in self.volunteer_experience:
                componentsschemas_volunteer_experience_list_item = (
                    componentsschemas_volunteer_experience_list_item_data.to_dict()
                )
                volunteer_experience.append(componentsschemas_volunteer_experience_list_item)

        else:
            volunteer_experience = self.volunteer_experience

        honors: list[dict[str, Any]] | None
        if isinstance(self.honors, list):
            honors = []
            for honors_type_0_item_data in self.honors:
                honors_type_0_item = honors_type_0_item_data.to_dict()
                honors.append(honors_type_0_item)

        else:
            honors = self.honors

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
                "counts": counts,
                "experience": experience,
                "education": education,
                "skills": skills,
                "certifications": certifications,
                "organizations": organizations,
                "languages": languages,
                "courses": courses,
                "volunteerExperience": volunteer_experience,
                "honors": honors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_item import CourseItem  # noqa: PLC0415
        from ..models.education_item import EducationItem  # noqa: PLC0415
        from ..models.honor_item import HonorItem  # noqa: PLC0415
        from ..models.image_variant import ImageVariant  # noqa: PLC0415
        from ..models.industry_reference_type_0 import IndustryReferenceType0  # noqa: PLC0415
        from ..models.industry_reference_type_1 import IndustryReferenceType1  # noqa: PLC0415
        from ..models.industry_reference_type_2 import IndustryReferenceType2  # noqa: PLC0415
        from ..models.language_item import LanguageItem  # noqa: PLC0415
        from ..models.locale import Locale  # noqa: PLC0415
        from ..models.organization_membership_item import OrganizationMembershipItem  # noqa: PLC0415
        from ..models.position_item import PositionItem  # noqa: PLC0415
        from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0  # noqa: PLC0415
        from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1  # noqa: PLC0415
        from ..models.profile_counts import ProfileCounts  # noqa: PLC0415
        from ..models.profile_location import ProfileLocation  # noqa: PLC0415
        from ..models.volunteer_experience_item import VolunteerExperienceItem  # noqa: PLC0415

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

        def _parse_counts(data: object) -> None | ProfileCounts:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = ProfileCounts.from_dict(data)

                return counts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProfileCounts, data)

        counts = _parse_counts(d.pop("counts"))

        def _parse_experience(data: object) -> list[PositionItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                experience_type_0 = []
                _experience_type_0 = data
                for componentsschemas_position_list_item_data in _experience_type_0:
                    componentsschemas_position_list_item = PositionItem.from_dict(
                        componentsschemas_position_list_item_data
                    )

                    experience_type_0.append(componentsschemas_position_list_item)

                return experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PositionItem] | None, data)

        experience = _parse_experience(d.pop("experience"))

        def _parse_education(data: object) -> list[EducationItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                education_type_0 = []
                _education_type_0 = data
                for componentsschemas_education_list_item_data in _education_type_0:
                    componentsschemas_education_list_item = EducationItem.from_dict(
                        componentsschemas_education_list_item_data
                    )

                    education_type_0.append(componentsschemas_education_list_item)

                return education_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EducationItem] | None, data)

        education = _parse_education(d.pop("education"))

        def _parse_skills(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = cast(list[str], data)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        skills = _parse_skills(d.pop("skills"))

        def _parse_certifications(
            data: object,
        ) -> list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                certifications_type_0 = []
                _certifications_type_0 = data
                for componentsschemas_profile_certification_list_item_data in _certifications_type_0:

                    def _parse_componentsschemas_profile_certification_list_item(
                        data: object,
                    ) -> Any | ProfileCertificationItemType0 | ProfileCertificationItemType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_profile_certification_item_type_0 = (
                                ProfileCertificationItemType0.from_dict(data)
                            )

                            return componentsschemas_profile_certification_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_profile_certification_item_type_1 = (
                                ProfileCertificationItemType1.from_dict(data)
                            )

                            return componentsschemas_profile_certification_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(Any | ProfileCertificationItemType0 | ProfileCertificationItemType1, data)

                    componentsschemas_profile_certification_list_item = (
                        _parse_componentsschemas_profile_certification_list_item(
                            componentsschemas_profile_certification_list_item_data
                        )
                    )

                    certifications_type_0.append(componentsschemas_profile_certification_list_item)

                return certifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1] | None, data)

        certifications = _parse_certifications(d.pop("certifications"))

        def _parse_organizations(data: object) -> list[OrganizationMembershipItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = []
                _organizations_type_0 = data
                for organizations_type_0_item_data in _organizations_type_0:
                    organizations_type_0_item = OrganizationMembershipItem.from_dict(organizations_type_0_item_data)

                    organizations_type_0.append(organizations_type_0_item)

                return organizations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrganizationMembershipItem] | None, data)

        organizations = _parse_organizations(d.pop("organizations"))

        def _parse_languages(data: object) -> list[LanguageItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = LanguageItem.from_dict(languages_type_0_item_data)

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LanguageItem] | None, data)

        languages = _parse_languages(d.pop("languages"))

        def _parse_courses(data: object) -> list[CourseItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                courses_type_0 = []
                _courses_type_0 = data
                for componentsschemas_course_list_item_data in _courses_type_0:
                    componentsschemas_course_list_item = CourseItem.from_dict(componentsschemas_course_list_item_data)

                    courses_type_0.append(componentsschemas_course_list_item)

                return courses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CourseItem] | None, data)

        courses = _parse_courses(d.pop("courses"))

        def _parse_volunteer_experience(data: object) -> list[VolunteerExperienceItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volunteer_experience_type_0 = []
                _volunteer_experience_type_0 = data
                for componentsschemas_volunteer_experience_list_item_data in _volunteer_experience_type_0:
                    componentsschemas_volunteer_experience_list_item = VolunteerExperienceItem.from_dict(
                        componentsschemas_volunteer_experience_list_item_data
                    )

                    volunteer_experience_type_0.append(componentsschemas_volunteer_experience_list_item)

                return volunteer_experience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerExperienceItem] | None, data)

        volunteer_experience = _parse_volunteer_experience(d.pop("volunteerExperience"))

        def _parse_honors(data: object) -> list[HonorItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                honors_type_0 = []
                _honors_type_0 = data
                for honors_type_0_item_data in _honors_type_0:
                    honors_type_0_item = HonorItem.from_dict(honors_type_0_item_data)

                    honors_type_0.append(honors_type_0_item)

                return honors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HonorItem] | None, data)

        honors = _parse_honors(d.pop("honors"))

        profile_details_data = cls(
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
            counts=counts,
            experience=experience,
            education=education,
            skills=skills,
            certifications=certifications,
            organizations=organizations,
            languages=languages,
            courses=courses,
            volunteer_experience=volunteer_experience,
            honors=honors,
        )

        return profile_details_data
