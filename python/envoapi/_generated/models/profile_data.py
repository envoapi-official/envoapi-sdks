from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.certification_item_type_0 import CertificationItemType0
    from ..models.certification_item_type_1 import CertificationItemType1
    from ..models.certification_item_type_2 import CertificationItemType2
    from ..models.company_reference_type_0 import CompanyReferenceType0
    from ..models.company_reference_type_1 import CompanyReferenceType1
    from ..models.company_reference_type_2 import CompanyReferenceType2
    from ..models.contact import Contact
    from ..models.course_item import CourseItem
    from ..models.education_item import EducationItem
    from ..models.honor_item import HonorItem
    from ..models.language_item import LanguageItem
    from ..models.organization_membership_item import OrganizationMembershipItem
    from ..models.position_item import PositionItem
    from ..models.profile import Profile
    from ..models.profile_counts import ProfileCounts
    from ..models.skill_item import SkillItem
    from ..models.volunteer_experience_item import VolunteerExperienceItem


T = TypeVar("T", bound="ProfileData")


@_attrs_define
class ProfileData:
    """
    Attributes:
        profile (Profile):
        counts (None | ProfileCounts):
        positions (list[PositionItem] | None):
        education (list[EducationItem] | None):
        skills (list[SkillItem] | None):
        certifications (list[CertificationItemType0 | CertificationItemType1 | CertificationItemType2] | None):
        organizations (list[OrganizationMembershipItem] | None):
        languages (list[LanguageItem] | None):
        courses (list[CourseItem] | None):
        volunteer_experience (list[VolunteerExperienceItem] | None):
        honors (list[HonorItem] | None):
        company_interests (list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2] | None):
        contact (Contact | None):
    """

    profile: Profile
    counts: None | ProfileCounts
    positions: list[PositionItem] | None
    education: list[EducationItem] | None
    skills: list[SkillItem] | None
    certifications: list[CertificationItemType0 | CertificationItemType1 | CertificationItemType2] | None
    organizations: list[OrganizationMembershipItem] | None
    languages: list[LanguageItem] | None
    courses: list[CourseItem] | None
    volunteer_experience: list[VolunteerExperienceItem] | None
    honors: list[HonorItem] | None
    company_interests: list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2] | None
    contact: Contact | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.certification_item_type_0 import CertificationItemType0  # noqa: PLC0415
        from ..models.certification_item_type_1 import CertificationItemType1  # noqa: PLC0415
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.contact import Contact  # noqa: PLC0415
        from ..models.profile_counts import ProfileCounts  # noqa: PLC0415

        profile = self.profile.to_dict()

        counts: dict[str, Any] | None
        if isinstance(self.counts, ProfileCounts):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

        positions: list[dict[str, Any]] | None
        if isinstance(self.positions, list):
            positions = []
            for componentsschemas_position_list_item_data in self.positions:
                componentsschemas_position_list_item = componentsschemas_position_list_item_data.to_dict()
                positions.append(componentsschemas_position_list_item)

        else:
            positions = self.positions

        education: list[dict[str, Any]] | None
        if isinstance(self.education, list):
            education = []
            for componentsschemas_education_list_item_data in self.education:
                componentsschemas_education_list_item = componentsschemas_education_list_item_data.to_dict()
                education.append(componentsschemas_education_list_item)

        else:
            education = self.education

        skills: list[dict[str, Any]] | None
        if isinstance(self.skills, list):
            skills = []
            for componentsschemas_skill_list_item_data in self.skills:
                componentsschemas_skill_list_item = componentsschemas_skill_list_item_data.to_dict()
                skills.append(componentsschemas_skill_list_item)

        else:
            skills = self.skills

        certifications: list[dict[str, Any]] | None
        if isinstance(self.certifications, list):
            certifications = []
            for componentsschemas_certification_list_item_data in self.certifications:
                componentsschemas_certification_list_item: dict[str, Any]
                if isinstance(componentsschemas_certification_list_item_data, CertificationItemType0):
                    componentsschemas_certification_list_item = componentsschemas_certification_list_item_data.to_dict()
                elif isinstance(componentsschemas_certification_list_item_data, CertificationItemType1):
                    componentsschemas_certification_list_item = componentsschemas_certification_list_item_data.to_dict()
                else:
                    componentsschemas_certification_list_item = componentsschemas_certification_list_item_data.to_dict()

                certifications.append(componentsschemas_certification_list_item)

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

        company_interests: list[dict[str, Any]] | None
        if isinstance(self.company_interests, list):
            company_interests = []
            for componentsschemas_company_interest_list_item_data in self.company_interests:
                componentsschemas_company_interest_list_item: dict[str, Any]
                if isinstance(componentsschemas_company_interest_list_item_data, CompanyReferenceType0):
                    componentsschemas_company_interest_list_item = (
                        componentsschemas_company_interest_list_item_data.to_dict()
                    )
                elif isinstance(componentsschemas_company_interest_list_item_data, CompanyReferenceType1):
                    componentsschemas_company_interest_list_item = (
                        componentsschemas_company_interest_list_item_data.to_dict()
                    )
                else:
                    componentsschemas_company_interest_list_item = (
                        componentsschemas_company_interest_list_item_data.to_dict()
                    )

                company_interests.append(componentsschemas_company_interest_list_item)

        else:
            company_interests = self.company_interests

        contact: dict[str, Any] | None
        if isinstance(self.contact, Contact):
            contact = self.contact.to_dict()
        else:
            contact = self.contact

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "profile": profile,
                "counts": counts,
                "positions": positions,
                "education": education,
                "skills": skills,
                "certifications": certifications,
                "organizations": organizations,
                "languages": languages,
                "courses": courses,
                "volunteerExperience": volunteer_experience,
                "honors": honors,
                "companyInterests": company_interests,
                "contact": contact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certification_item_type_0 import CertificationItemType0  # noqa: PLC0415
        from ..models.certification_item_type_1 import CertificationItemType1  # noqa: PLC0415
        from ..models.certification_item_type_2 import CertificationItemType2  # noqa: PLC0415
        from ..models.company_reference_type_0 import CompanyReferenceType0  # noqa: PLC0415
        from ..models.company_reference_type_1 import CompanyReferenceType1  # noqa: PLC0415
        from ..models.company_reference_type_2 import CompanyReferenceType2  # noqa: PLC0415
        from ..models.contact import Contact  # noqa: PLC0415
        from ..models.course_item import CourseItem  # noqa: PLC0415
        from ..models.education_item import EducationItem  # noqa: PLC0415
        from ..models.honor_item import HonorItem  # noqa: PLC0415
        from ..models.language_item import LanguageItem  # noqa: PLC0415
        from ..models.organization_membership_item import OrganizationMembershipItem  # noqa: PLC0415
        from ..models.position_item import PositionItem  # noqa: PLC0415
        from ..models.profile import Profile  # noqa: PLC0415
        from ..models.profile_counts import ProfileCounts  # noqa: PLC0415
        from ..models.skill_item import SkillItem  # noqa: PLC0415
        from ..models.volunteer_experience_item import VolunteerExperienceItem  # noqa: PLC0415

        d = dict(src_dict)
        profile = Profile.from_dict(d.pop("profile"))

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

        def _parse_positions(data: object) -> list[PositionItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positions_type_0 = []
                _positions_type_0 = data
                for componentsschemas_position_list_item_data in _positions_type_0:
                    componentsschemas_position_list_item = PositionItem.from_dict(
                        componentsschemas_position_list_item_data
                    )

                    positions_type_0.append(componentsschemas_position_list_item)

                return positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PositionItem] | None, data)

        positions = _parse_positions(d.pop("positions"))

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

        def _parse_skills(data: object) -> list[SkillItem] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = []
                _skills_type_0 = data
                for componentsschemas_skill_list_item_data in _skills_type_0:
                    componentsschemas_skill_list_item = SkillItem.from_dict(componentsschemas_skill_list_item_data)

                    skills_type_0.append(componentsschemas_skill_list_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SkillItem] | None, data)

        skills = _parse_skills(d.pop("skills"))

        def _parse_certifications(
            data: object,
        ) -> list[CertificationItemType0 | CertificationItemType1 | CertificationItemType2] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                certifications_type_0 = []
                _certifications_type_0 = data
                for componentsschemas_certification_list_item_data in _certifications_type_0:

                    def _parse_componentsschemas_certification_list_item(
                        data: object,
                    ) -> CertificationItemType0 | CertificationItemType1 | CertificationItemType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_certification_item_type_0 = CertificationItemType0.from_dict(data)

                            return componentsschemas_certification_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_certification_item_type_1 = CertificationItemType1.from_dict(data)

                            return componentsschemas_certification_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_certification_item_type_2 = CertificationItemType2.from_dict(data)

                        return componentsschemas_certification_item_type_2

                    componentsschemas_certification_list_item = _parse_componentsschemas_certification_list_item(
                        componentsschemas_certification_list_item_data
                    )

                    certifications_type_0.append(componentsschemas_certification_list_item)

                return certifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CertificationItemType0 | CertificationItemType1 | CertificationItemType2] | None, data)

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

        def _parse_company_interests(
            data: object,
        ) -> list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                company_interests_type_0 = []
                _company_interests_type_0 = data
                for componentsschemas_company_interest_list_item_data in _company_interests_type_0:

                    def _parse_componentsschemas_company_interest_list_item(
                        data: object,
                    ) -> CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_company_reference_type_0 = CompanyReferenceType0.from_dict(data)

                            return componentsschemas_company_reference_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_company_reference_type_1 = CompanyReferenceType1.from_dict(data)

                            return componentsschemas_company_reference_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_company_reference_type_2 = CompanyReferenceType2.from_dict(data)

                        return componentsschemas_company_reference_type_2

                    componentsschemas_company_interest_list_item = _parse_componentsschemas_company_interest_list_item(
                        componentsschemas_company_interest_list_item_data
                    )

                    company_interests_type_0.append(componentsschemas_company_interest_list_item)

                return company_interests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CompanyReferenceType0 | CompanyReferenceType1 | CompanyReferenceType2] | None, data)

        company_interests = _parse_company_interests(d.pop("companyInterests"))

        def _parse_contact(data: object) -> Contact | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_type_0 = Contact.from_dict(data)

                return contact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Contact | None, data)

        contact = _parse_contact(d.pop("contact"))

        profile_data = cls(
            profile=profile,
            counts=counts,
            positions=positions,
            education=education,
            skills=skills,
            certifications=certifications,
            organizations=organizations,
            languages=languages,
            courses=courses,
            volunteer_experience=volunteer_experience,
            honors=honors,
            company_interests=company_interests,
            contact=contact,
        )

        return profile_data
