from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.certification_section_meta_type_0_type_0 import CertificationSectionMetaType0Type0
    from ..models.certification_section_meta_type_0_type_1 import CertificationSectionMetaType0Type1
    from ..models.certification_section_meta_type_1 import CertificationSectionMetaType1
    from ..models.company_interest_section_meta_type_0_type_0_type_0 import CompanyInterestSectionMetaType0Type0Type0
    from ..models.company_interest_section_meta_type_0_type_0_type_1 import CompanyInterestSectionMetaType0Type0Type1
    from ..models.company_interest_section_meta_type_0_type_1 import CompanyInterestSectionMetaType0Type1
    from ..models.contact_section_meta_type_0_type_0 import ContactSectionMetaType0Type0
    from ..models.contact_section_meta_type_0_type_1 import ContactSectionMetaType0Type1
    from ..models.contact_section_meta_type_1 import ContactSectionMetaType1
    from ..models.course_section_meta_type_0_type_0 import CourseSectionMetaType0Type0
    from ..models.course_section_meta_type_0_type_1 import CourseSectionMetaType0Type1
    from ..models.course_section_meta_type_1 import CourseSectionMetaType1
    from ..models.education_section_meta_type_0_type_0 import EducationSectionMetaType0Type0
    from ..models.education_section_meta_type_0_type_1 import EducationSectionMetaType0Type1
    from ..models.education_section_meta_type_1 import EducationSectionMetaType1
    from ..models.failed_section_meta import FailedSectionMeta
    from ..models.honor_section_meta_type_0_type_0 import HonorSectionMetaType0Type0
    from ..models.honor_section_meta_type_0_type_1 import HonorSectionMetaType0Type1
    from ..models.honor_section_meta_type_1 import HonorSectionMetaType1
    from ..models.language_section_meta_type_0_type_0 import LanguageSectionMetaType0Type0
    from ..models.language_section_meta_type_0_type_1 import LanguageSectionMetaType0Type1
    from ..models.language_section_meta_type_1 import LanguageSectionMetaType1
    from ..models.not_requested_section_meta import NotRequestedSectionMeta
    from ..models.organization_section_meta_type_0_type_0 import OrganizationSectionMetaType0Type0
    from ..models.organization_section_meta_type_0_type_1 import OrganizationSectionMetaType0Type1
    from ..models.organization_section_meta_type_1 import OrganizationSectionMetaType1
    from ..models.position_section_meta_type_0_type_0 import PositionSectionMetaType0Type0
    from ..models.position_section_meta_type_0_type_1 import PositionSectionMetaType0Type1
    from ..models.position_section_meta_type_1 import PositionSectionMetaType1
    from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0
    from ..models.required_core_section_meta_type_1 import RequiredCoreSectionMetaType1
    from ..models.singleton_section_meta_type_0_type_0 import SingletonSectionMetaType0Type0
    from ..models.singleton_section_meta_type_0_type_1 import SingletonSectionMetaType0Type1
    from ..models.singleton_section_meta_type_1 import SingletonSectionMetaType1
    from ..models.skill_section_meta_type_0 import SkillSectionMetaType0
    from ..models.skill_section_meta_type_1 import SkillSectionMetaType1
    from ..models.skill_section_meta_type_2 import SkillSectionMetaType2
    from ..models.skill_section_meta_type_3 import SkillSectionMetaType3
    from ..models.skill_section_meta_type_4 import SkillSectionMetaType4
    from ..models.skipped_section_meta import SkippedSectionMeta
    from ..models.volunteer_experience_section_meta_type_0_type_0 import VolunteerExperienceSectionMetaType0Type0
    from ..models.volunteer_experience_section_meta_type_0_type_1 import VolunteerExperienceSectionMetaType0Type1
    from ..models.volunteer_experience_section_meta_type_1 import VolunteerExperienceSectionMetaType1


T = TypeVar("T", bound="ProfileSections")


@_attrs_define
class ProfileSections:
    """
    Attributes:
        profile (RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1):
        counts (FailedSectionMeta | SingletonSectionMetaType0Type0 | SingletonSectionMetaType0Type1 |
            SingletonSectionMetaType1 | SkippedSectionMeta):
        positions (FailedSectionMeta | PositionSectionMetaType0Type0 | PositionSectionMetaType0Type1 |
            PositionSectionMetaType1 | SkippedSectionMeta):
        education (EducationSectionMetaType0Type0 | EducationSectionMetaType0Type1 | EducationSectionMetaType1 |
            FailedSectionMeta | SkippedSectionMeta):
        skills (SkillSectionMetaType0 | SkillSectionMetaType1 | SkillSectionMetaType2 | SkillSectionMetaType3 |
            SkillSectionMetaType4):
        certifications (CertificationSectionMetaType0Type0 | CertificationSectionMetaType0Type1 |
            CertificationSectionMetaType1 | FailedSectionMeta | SkippedSectionMeta):
        organizations (FailedSectionMeta | OrganizationSectionMetaType0Type0 | OrganizationSectionMetaType0Type1 |
            OrganizationSectionMetaType1 | SkippedSectionMeta):
        languages (FailedSectionMeta | LanguageSectionMetaType0Type0 | LanguageSectionMetaType0Type1 |
            LanguageSectionMetaType1 | SkippedSectionMeta):
        courses (CourseSectionMetaType0Type0 | CourseSectionMetaType0Type1 | CourseSectionMetaType1 | FailedSectionMeta
            | SkippedSectionMeta):
        volunteer_experience (FailedSectionMeta | SkippedSectionMeta | VolunteerExperienceSectionMetaType0Type0 |
            VolunteerExperienceSectionMetaType0Type1 | VolunteerExperienceSectionMetaType1):
        honors (FailedSectionMeta | HonorSectionMetaType0Type0 | HonorSectionMetaType0Type1 | HonorSectionMetaType1 |
            SkippedSectionMeta):
        company_interests (CompanyInterestSectionMetaType0Type0Type0 | CompanyInterestSectionMetaType0Type0Type1 |
            CompanyInterestSectionMetaType0Type1 | FailedSectionMeta | NotRequestedSectionMeta | SkippedSectionMeta):
        contact (ContactSectionMetaType0Type0 | ContactSectionMetaType0Type1 | ContactSectionMetaType1 |
            FailedSectionMeta | NotRequestedSectionMeta | SkippedSectionMeta):
    """

    profile: RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1
    counts: (
        FailedSectionMeta
        | SingletonSectionMetaType0Type0
        | SingletonSectionMetaType0Type1
        | SingletonSectionMetaType1
        | SkippedSectionMeta
    )
    positions: (
        FailedSectionMeta
        | PositionSectionMetaType0Type0
        | PositionSectionMetaType0Type1
        | PositionSectionMetaType1
        | SkippedSectionMeta
    )
    education: (
        EducationSectionMetaType0Type0
        | EducationSectionMetaType0Type1
        | EducationSectionMetaType1
        | FailedSectionMeta
        | SkippedSectionMeta
    )
    skills: (
        SkillSectionMetaType0
        | SkillSectionMetaType1
        | SkillSectionMetaType2
        | SkillSectionMetaType3
        | SkillSectionMetaType4
    )
    certifications: (
        CertificationSectionMetaType0Type0
        | CertificationSectionMetaType0Type1
        | CertificationSectionMetaType1
        | FailedSectionMeta
        | SkippedSectionMeta
    )
    organizations: (
        FailedSectionMeta
        | OrganizationSectionMetaType0Type0
        | OrganizationSectionMetaType0Type1
        | OrganizationSectionMetaType1
        | SkippedSectionMeta
    )
    languages: (
        FailedSectionMeta
        | LanguageSectionMetaType0Type0
        | LanguageSectionMetaType0Type1
        | LanguageSectionMetaType1
        | SkippedSectionMeta
    )
    courses: (
        CourseSectionMetaType0Type0
        | CourseSectionMetaType0Type1
        | CourseSectionMetaType1
        | FailedSectionMeta
        | SkippedSectionMeta
    )
    volunteer_experience: (
        FailedSectionMeta
        | SkippedSectionMeta
        | VolunteerExperienceSectionMetaType0Type0
        | VolunteerExperienceSectionMetaType0Type1
        | VolunteerExperienceSectionMetaType1
    )
    honors: (
        FailedSectionMeta
        | HonorSectionMetaType0Type0
        | HonorSectionMetaType0Type1
        | HonorSectionMetaType1
        | SkippedSectionMeta
    )
    company_interests: (
        CompanyInterestSectionMetaType0Type0Type0
        | CompanyInterestSectionMetaType0Type0Type1
        | CompanyInterestSectionMetaType0Type1
        | FailedSectionMeta
        | NotRequestedSectionMeta
        | SkippedSectionMeta
    )
    contact: (
        ContactSectionMetaType0Type0
        | ContactSectionMetaType0Type1
        | ContactSectionMetaType1
        | FailedSectionMeta
        | NotRequestedSectionMeta
        | SkippedSectionMeta
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.certification_section_meta_type_0_type_0 import (
            CertificationSectionMetaType0Type0,  # noqa: PLC0415
        )
        from ..models.certification_section_meta_type_0_type_1 import (
            CertificationSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.certification_section_meta_type_1 import CertificationSectionMetaType1  # noqa: PLC0415
        from ..models.company_interest_section_meta_type_0_type_0_type_0 import (
            CompanyInterestSectionMetaType0Type0Type0,  # noqa: PLC0415
        )
        from ..models.company_interest_section_meta_type_0_type_0_type_1 import (
            CompanyInterestSectionMetaType0Type0Type1,  # noqa: PLC0415
        )
        from ..models.company_interest_section_meta_type_0_type_1 import (
            CompanyInterestSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.contact_section_meta_type_0_type_0 import ContactSectionMetaType0Type0  # noqa: PLC0415
        from ..models.contact_section_meta_type_0_type_1 import ContactSectionMetaType0Type1  # noqa: PLC0415
        from ..models.contact_section_meta_type_1 import ContactSectionMetaType1  # noqa: PLC0415
        from ..models.course_section_meta_type_0_type_0 import CourseSectionMetaType0Type0  # noqa: PLC0415
        from ..models.course_section_meta_type_0_type_1 import CourseSectionMetaType0Type1  # noqa: PLC0415
        from ..models.course_section_meta_type_1 import CourseSectionMetaType1  # noqa: PLC0415
        from ..models.education_section_meta_type_0_type_0 import EducationSectionMetaType0Type0  # noqa: PLC0415
        from ..models.education_section_meta_type_0_type_1 import EducationSectionMetaType0Type1  # noqa: PLC0415
        from ..models.education_section_meta_type_1 import EducationSectionMetaType1  # noqa: PLC0415
        from ..models.failed_section_meta import FailedSectionMeta  # noqa: PLC0415
        from ..models.honor_section_meta_type_0_type_0 import HonorSectionMetaType0Type0  # noqa: PLC0415
        from ..models.honor_section_meta_type_0_type_1 import HonorSectionMetaType0Type1  # noqa: PLC0415
        from ..models.honor_section_meta_type_1 import HonorSectionMetaType1  # noqa: PLC0415
        from ..models.language_section_meta_type_0_type_0 import LanguageSectionMetaType0Type0  # noqa: PLC0415
        from ..models.language_section_meta_type_0_type_1 import LanguageSectionMetaType0Type1  # noqa: PLC0415
        from ..models.language_section_meta_type_1 import LanguageSectionMetaType1  # noqa: PLC0415
        from ..models.organization_section_meta_type_0_type_0 import OrganizationSectionMetaType0Type0  # noqa: PLC0415
        from ..models.organization_section_meta_type_0_type_1 import OrganizationSectionMetaType0Type1  # noqa: PLC0415
        from ..models.organization_section_meta_type_1 import OrganizationSectionMetaType1  # noqa: PLC0415
        from ..models.position_section_meta_type_0_type_0 import PositionSectionMetaType0Type0  # noqa: PLC0415
        from ..models.position_section_meta_type_0_type_1 import PositionSectionMetaType0Type1  # noqa: PLC0415
        from ..models.position_section_meta_type_1 import PositionSectionMetaType1  # noqa: PLC0415
        from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0  # noqa: PLC0415
        from ..models.singleton_section_meta_type_0_type_0 import SingletonSectionMetaType0Type0  # noqa: PLC0415
        from ..models.singleton_section_meta_type_0_type_1 import SingletonSectionMetaType0Type1  # noqa: PLC0415
        from ..models.singleton_section_meta_type_1 import SingletonSectionMetaType1  # noqa: PLC0415
        from ..models.skill_section_meta_type_0 import SkillSectionMetaType0  # noqa: PLC0415
        from ..models.skill_section_meta_type_1 import SkillSectionMetaType1  # noqa: PLC0415
        from ..models.skill_section_meta_type_2 import SkillSectionMetaType2  # noqa: PLC0415
        from ..models.skill_section_meta_type_3 import SkillSectionMetaType3  # noqa: PLC0415
        from ..models.skipped_section_meta import SkippedSectionMeta  # noqa: PLC0415
        from ..models.volunteer_experience_section_meta_type_0_type_0 import (
            VolunteerExperienceSectionMetaType0Type0,  # noqa: PLC0415
        )
        from ..models.volunteer_experience_section_meta_type_0_type_1 import (
            VolunteerExperienceSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.volunteer_experience_section_meta_type_1 import (
            VolunteerExperienceSectionMetaType1,  # noqa: PLC0415
        )

        profile: dict[str, Any]
        if isinstance(self.profile, RequiredCoreSectionMetaType0):
            profile = self.profile.to_dict()
        else:
            profile = self.profile.to_dict()

        counts: dict[str, Any]
        if isinstance(self.counts, SingletonSectionMetaType0Type0):
            counts = self.counts.to_dict()
        elif isinstance(self.counts, SingletonSectionMetaType0Type1):
            counts = self.counts.to_dict()
        elif isinstance(self.counts, SingletonSectionMetaType1):
            counts = self.counts.to_dict()
        elif isinstance(self.counts, FailedSectionMeta):
            counts = self.counts.to_dict()
        else:
            counts = self.counts.to_dict()

        positions: dict[str, Any]
        if isinstance(self.positions, PositionSectionMetaType0Type0):
            positions = self.positions.to_dict()
        elif isinstance(self.positions, PositionSectionMetaType0Type1):
            positions = self.positions.to_dict()
        elif isinstance(self.positions, PositionSectionMetaType1):
            positions = self.positions.to_dict()
        elif isinstance(self.positions, FailedSectionMeta):
            positions = self.positions.to_dict()
        else:
            positions = self.positions.to_dict()

        education: dict[str, Any]
        if isinstance(self.education, EducationSectionMetaType0Type0):
            education = self.education.to_dict()
        elif isinstance(self.education, EducationSectionMetaType0Type1):
            education = self.education.to_dict()
        elif isinstance(self.education, EducationSectionMetaType1):
            education = self.education.to_dict()
        elif isinstance(self.education, FailedSectionMeta):
            education = self.education.to_dict()
        else:
            education = self.education.to_dict()

        skills: dict[str, Any]
        if isinstance(self.skills, SkillSectionMetaType0):
            skills = self.skills.to_dict()
        elif isinstance(self.skills, SkillSectionMetaType1):
            skills = self.skills.to_dict()
        elif isinstance(self.skills, SkillSectionMetaType2):
            skills = self.skills.to_dict()
        elif isinstance(self.skills, SkillSectionMetaType3):
            skills = self.skills.to_dict()
        else:
            skills = self.skills.to_dict()

        certifications: dict[str, Any]
        if isinstance(self.certifications, CertificationSectionMetaType0Type0):
            certifications = self.certifications.to_dict()
        elif isinstance(self.certifications, CertificationSectionMetaType0Type1):
            certifications = self.certifications.to_dict()
        elif isinstance(self.certifications, CertificationSectionMetaType1):
            certifications = self.certifications.to_dict()
        elif isinstance(self.certifications, FailedSectionMeta):
            certifications = self.certifications.to_dict()
        else:
            certifications = self.certifications.to_dict()

        organizations: dict[str, Any]
        if isinstance(self.organizations, OrganizationSectionMetaType0Type0):
            organizations = self.organizations.to_dict()
        elif isinstance(self.organizations, OrganizationSectionMetaType0Type1):
            organizations = self.organizations.to_dict()
        elif isinstance(self.organizations, OrganizationSectionMetaType1):
            organizations = self.organizations.to_dict()
        elif isinstance(self.organizations, FailedSectionMeta):
            organizations = self.organizations.to_dict()
        else:
            organizations = self.organizations.to_dict()

        languages: dict[str, Any]
        if isinstance(self.languages, LanguageSectionMetaType0Type0):
            languages = self.languages.to_dict()
        elif isinstance(self.languages, LanguageSectionMetaType0Type1):
            languages = self.languages.to_dict()
        elif isinstance(self.languages, LanguageSectionMetaType1):
            languages = self.languages.to_dict()
        elif isinstance(self.languages, FailedSectionMeta):
            languages = self.languages.to_dict()
        else:
            languages = self.languages.to_dict()

        courses: dict[str, Any]
        if isinstance(self.courses, CourseSectionMetaType0Type0):
            courses = self.courses.to_dict()
        elif isinstance(self.courses, CourseSectionMetaType0Type1):
            courses = self.courses.to_dict()
        elif isinstance(self.courses, CourseSectionMetaType1):
            courses = self.courses.to_dict()
        elif isinstance(self.courses, FailedSectionMeta):
            courses = self.courses.to_dict()
        else:
            courses = self.courses.to_dict()

        volunteer_experience: dict[str, Any]
        if isinstance(self.volunteer_experience, VolunteerExperienceSectionMetaType0Type0):
            volunteer_experience = self.volunteer_experience.to_dict()
        elif isinstance(self.volunteer_experience, VolunteerExperienceSectionMetaType0Type1):
            volunteer_experience = self.volunteer_experience.to_dict()
        elif isinstance(self.volunteer_experience, VolunteerExperienceSectionMetaType1):
            volunteer_experience = self.volunteer_experience.to_dict()
        elif isinstance(self.volunteer_experience, FailedSectionMeta):
            volunteer_experience = self.volunteer_experience.to_dict()
        else:
            volunteer_experience = self.volunteer_experience.to_dict()

        honors: dict[str, Any]
        if isinstance(self.honors, HonorSectionMetaType0Type0):
            honors = self.honors.to_dict()
        elif isinstance(self.honors, HonorSectionMetaType0Type1):
            honors = self.honors.to_dict()
        elif isinstance(self.honors, HonorSectionMetaType1):
            honors = self.honors.to_dict()
        elif isinstance(self.honors, FailedSectionMeta):
            honors = self.honors.to_dict()
        else:
            honors = self.honors.to_dict()

        company_interests: dict[str, Any]
        if isinstance(self.company_interests, CompanyInterestSectionMetaType0Type0Type0):
            company_interests = self.company_interests.to_dict()
        elif isinstance(self.company_interests, CompanyInterestSectionMetaType0Type0Type1):
            company_interests = self.company_interests.to_dict()
        elif isinstance(self.company_interests, CompanyInterestSectionMetaType0Type1):
            company_interests = self.company_interests.to_dict()
        elif isinstance(self.company_interests, FailedSectionMeta):
            company_interests = self.company_interests.to_dict()
        elif isinstance(self.company_interests, SkippedSectionMeta):
            company_interests = self.company_interests.to_dict()
        else:
            company_interests = self.company_interests.to_dict()

        contact: dict[str, Any]
        if isinstance(self.contact, ContactSectionMetaType0Type0):
            contact = self.contact.to_dict()
        elif isinstance(self.contact, ContactSectionMetaType0Type1):
            contact = self.contact.to_dict()
        elif isinstance(self.contact, ContactSectionMetaType1):
            contact = self.contact.to_dict()
        elif isinstance(self.contact, FailedSectionMeta):
            contact = self.contact.to_dict()
        elif isinstance(self.contact, SkippedSectionMeta):
            contact = self.contact.to_dict()
        else:
            contact = self.contact.to_dict()

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
        from ..models.certification_section_meta_type_0_type_0 import (
            CertificationSectionMetaType0Type0,  # noqa: PLC0415
        )
        from ..models.certification_section_meta_type_0_type_1 import (
            CertificationSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.certification_section_meta_type_1 import CertificationSectionMetaType1  # noqa: PLC0415
        from ..models.company_interest_section_meta_type_0_type_0_type_0 import (
            CompanyInterestSectionMetaType0Type0Type0,  # noqa: PLC0415
        )
        from ..models.company_interest_section_meta_type_0_type_0_type_1 import (
            CompanyInterestSectionMetaType0Type0Type1,  # noqa: PLC0415
        )
        from ..models.company_interest_section_meta_type_0_type_1 import (
            CompanyInterestSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.contact_section_meta_type_0_type_0 import ContactSectionMetaType0Type0  # noqa: PLC0415
        from ..models.contact_section_meta_type_0_type_1 import ContactSectionMetaType0Type1  # noqa: PLC0415
        from ..models.contact_section_meta_type_1 import ContactSectionMetaType1  # noqa: PLC0415
        from ..models.course_section_meta_type_0_type_0 import CourseSectionMetaType0Type0  # noqa: PLC0415
        from ..models.course_section_meta_type_0_type_1 import CourseSectionMetaType0Type1  # noqa: PLC0415
        from ..models.course_section_meta_type_1 import CourseSectionMetaType1  # noqa: PLC0415
        from ..models.education_section_meta_type_0_type_0 import EducationSectionMetaType0Type0  # noqa: PLC0415
        from ..models.education_section_meta_type_0_type_1 import EducationSectionMetaType0Type1  # noqa: PLC0415
        from ..models.education_section_meta_type_1 import EducationSectionMetaType1  # noqa: PLC0415
        from ..models.failed_section_meta import FailedSectionMeta  # noqa: PLC0415
        from ..models.honor_section_meta_type_0_type_0 import HonorSectionMetaType0Type0  # noqa: PLC0415
        from ..models.honor_section_meta_type_0_type_1 import HonorSectionMetaType0Type1  # noqa: PLC0415
        from ..models.honor_section_meta_type_1 import HonorSectionMetaType1  # noqa: PLC0415
        from ..models.language_section_meta_type_0_type_0 import LanguageSectionMetaType0Type0  # noqa: PLC0415
        from ..models.language_section_meta_type_0_type_1 import LanguageSectionMetaType0Type1  # noqa: PLC0415
        from ..models.language_section_meta_type_1 import LanguageSectionMetaType1  # noqa: PLC0415
        from ..models.not_requested_section_meta import NotRequestedSectionMeta  # noqa: PLC0415
        from ..models.organization_section_meta_type_0_type_0 import OrganizationSectionMetaType0Type0  # noqa: PLC0415
        from ..models.organization_section_meta_type_0_type_1 import OrganizationSectionMetaType0Type1  # noqa: PLC0415
        from ..models.organization_section_meta_type_1 import OrganizationSectionMetaType1  # noqa: PLC0415
        from ..models.position_section_meta_type_0_type_0 import PositionSectionMetaType0Type0  # noqa: PLC0415
        from ..models.position_section_meta_type_0_type_1 import PositionSectionMetaType0Type1  # noqa: PLC0415
        from ..models.position_section_meta_type_1 import PositionSectionMetaType1  # noqa: PLC0415
        from ..models.required_core_section_meta_type_0 import RequiredCoreSectionMetaType0  # noqa: PLC0415
        from ..models.required_core_section_meta_type_1 import RequiredCoreSectionMetaType1  # noqa: PLC0415
        from ..models.singleton_section_meta_type_0_type_0 import SingletonSectionMetaType0Type0  # noqa: PLC0415
        from ..models.singleton_section_meta_type_0_type_1 import SingletonSectionMetaType0Type1  # noqa: PLC0415
        from ..models.singleton_section_meta_type_1 import SingletonSectionMetaType1  # noqa: PLC0415
        from ..models.skill_section_meta_type_0 import SkillSectionMetaType0  # noqa: PLC0415
        from ..models.skill_section_meta_type_1 import SkillSectionMetaType1  # noqa: PLC0415
        from ..models.skill_section_meta_type_2 import SkillSectionMetaType2  # noqa: PLC0415
        from ..models.skill_section_meta_type_3 import SkillSectionMetaType3  # noqa: PLC0415
        from ..models.skill_section_meta_type_4 import SkillSectionMetaType4  # noqa: PLC0415
        from ..models.skipped_section_meta import SkippedSectionMeta  # noqa: PLC0415
        from ..models.volunteer_experience_section_meta_type_0_type_0 import (
            VolunteerExperienceSectionMetaType0Type0,  # noqa: PLC0415
        )
        from ..models.volunteer_experience_section_meta_type_0_type_1 import (
            VolunteerExperienceSectionMetaType0Type1,  # noqa: PLC0415
        )
        from ..models.volunteer_experience_section_meta_type_1 import (
            VolunteerExperienceSectionMetaType1,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_profile(data: object) -> RequiredCoreSectionMetaType0 | RequiredCoreSectionMetaType1:
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

        profile = _parse_profile(d.pop("profile"))

        def _parse_counts(
            data: object,
        ) -> (
            FailedSectionMeta
            | SingletonSectionMetaType0Type0
            | SingletonSectionMetaType0Type1
            | SingletonSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_singleton_section_meta_type_0_type_0 = SingletonSectionMetaType0Type0.from_dict(data)

                return componentsschemas_singleton_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_singleton_section_meta_type_0_type_1 = SingletonSectionMetaType0Type1.from_dict(data)

                return componentsschemas_singleton_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_singleton_section_meta_type_1 = SingletonSectionMetaType1.from_dict(data)

                return componentsschemas_singleton_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_singleton_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_singleton_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_singleton_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_singleton_section_meta_type_3

        counts = _parse_counts(d.pop("counts"))

        def _parse_positions(
            data: object,
        ) -> (
            FailedSectionMeta
            | PositionSectionMetaType0Type0
            | PositionSectionMetaType0Type1
            | PositionSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_position_section_meta_type_0_type_0 = PositionSectionMetaType0Type0.from_dict(data)

                return componentsschemas_position_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_position_section_meta_type_0_type_1 = PositionSectionMetaType0Type1.from_dict(data)

                return componentsschemas_position_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_position_section_meta_type_1 = PositionSectionMetaType1.from_dict(data)

                return componentsschemas_position_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_position_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_position_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_position_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_position_section_meta_type_3

        positions = _parse_positions(d.pop("positions"))

        def _parse_education(
            data: object,
        ) -> (
            EducationSectionMetaType0Type0
            | EducationSectionMetaType0Type1
            | EducationSectionMetaType1
            | FailedSectionMeta
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_section_meta_type_0_type_0 = EducationSectionMetaType0Type0.from_dict(data)

                return componentsschemas_education_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_section_meta_type_0_type_1 = EducationSectionMetaType0Type1.from_dict(data)

                return componentsschemas_education_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_section_meta_type_1 = EducationSectionMetaType1.from_dict(data)

                return componentsschemas_education_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_education_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_education_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_education_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_education_section_meta_type_3

        education = _parse_education(d.pop("education"))

        def _parse_skills(
            data: object,
        ) -> (
            SkillSectionMetaType0
            | SkillSectionMetaType1
            | SkillSectionMetaType2
            | SkillSectionMetaType3
            | SkillSectionMetaType4
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_skill_section_meta_type_0 = SkillSectionMetaType0.from_dict(data)

                return componentsschemas_skill_section_meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_skill_section_meta_type_1 = SkillSectionMetaType1.from_dict(data)

                return componentsschemas_skill_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_skill_section_meta_type_2 = SkillSectionMetaType2.from_dict(data)

                return componentsschemas_skill_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_skill_section_meta_type_3 = SkillSectionMetaType3.from_dict(data)

                return componentsschemas_skill_section_meta_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_skill_section_meta_type_4 = SkillSectionMetaType4.from_dict(data)

            return componentsschemas_skill_section_meta_type_4

        skills = _parse_skills(d.pop("skills"))

        def _parse_certifications(
            data: object,
        ) -> (
            CertificationSectionMetaType0Type0
            | CertificationSectionMetaType0Type1
            | CertificationSectionMetaType1
            | FailedSectionMeta
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_certification_section_meta_type_0_type_0 = (
                    CertificationSectionMetaType0Type0.from_dict(data)
                )

                return componentsschemas_certification_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_certification_section_meta_type_0_type_1 = (
                    CertificationSectionMetaType0Type1.from_dict(data)
                )

                return componentsschemas_certification_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_certification_section_meta_type_1 = CertificationSectionMetaType1.from_dict(data)

                return componentsschemas_certification_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_certification_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_certification_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_certification_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_certification_section_meta_type_3

        certifications = _parse_certifications(d.pop("certifications"))

        def _parse_organizations(
            data: object,
        ) -> (
            FailedSectionMeta
            | OrganizationSectionMetaType0Type0
            | OrganizationSectionMetaType0Type1
            | OrganizationSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_section_meta_type_0_type_0 = OrganizationSectionMetaType0Type0.from_dict(
                    data
                )

                return componentsschemas_organization_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_section_meta_type_0_type_1 = OrganizationSectionMetaType0Type1.from_dict(
                    data
                )

                return componentsschemas_organization_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_section_meta_type_1 = OrganizationSectionMetaType1.from_dict(data)

                return componentsschemas_organization_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_organization_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_organization_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_organization_section_meta_type_3

        organizations = _parse_organizations(d.pop("organizations"))

        def _parse_languages(
            data: object,
        ) -> (
            FailedSectionMeta
            | LanguageSectionMetaType0Type0
            | LanguageSectionMetaType0Type1
            | LanguageSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_language_section_meta_type_0_type_0 = LanguageSectionMetaType0Type0.from_dict(data)

                return componentsschemas_language_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_language_section_meta_type_0_type_1 = LanguageSectionMetaType0Type1.from_dict(data)

                return componentsschemas_language_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_language_section_meta_type_1 = LanguageSectionMetaType1.from_dict(data)

                return componentsschemas_language_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_language_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_language_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_language_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_language_section_meta_type_3

        languages = _parse_languages(d.pop("languages"))

        def _parse_courses(
            data: object,
        ) -> (
            CourseSectionMetaType0Type0
            | CourseSectionMetaType0Type1
            | CourseSectionMetaType1
            | FailedSectionMeta
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_section_meta_type_0_type_0 = CourseSectionMetaType0Type0.from_dict(data)

                return componentsschemas_course_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_section_meta_type_0_type_1 = CourseSectionMetaType0Type1.from_dict(data)

                return componentsschemas_course_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_section_meta_type_1 = CourseSectionMetaType1.from_dict(data)

                return componentsschemas_course_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_course_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_course_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_course_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_course_section_meta_type_3

        courses = _parse_courses(d.pop("courses"))

        def _parse_volunteer_experience(
            data: object,
        ) -> (
            FailedSectionMeta
            | SkippedSectionMeta
            | VolunteerExperienceSectionMetaType0Type0
            | VolunteerExperienceSectionMetaType0Type1
            | VolunteerExperienceSectionMetaType1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_volunteer_experience_section_meta_type_0_type_0 = (
                    VolunteerExperienceSectionMetaType0Type0.from_dict(data)
                )

                return componentsschemas_volunteer_experience_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_volunteer_experience_section_meta_type_0_type_1 = (
                    VolunteerExperienceSectionMetaType0Type1.from_dict(data)
                )

                return componentsschemas_volunteer_experience_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_volunteer_experience_section_meta_type_1 = (
                    VolunteerExperienceSectionMetaType1.from_dict(data)
                )

                return componentsschemas_volunteer_experience_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_volunteer_experience_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_volunteer_experience_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_volunteer_experience_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_volunteer_experience_section_meta_type_3

        volunteer_experience = _parse_volunteer_experience(d.pop("volunteerExperience"))

        def _parse_honors(
            data: object,
        ) -> (
            FailedSectionMeta
            | HonorSectionMetaType0Type0
            | HonorSectionMetaType0Type1
            | HonorSectionMetaType1
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_honor_section_meta_type_0_type_0 = HonorSectionMetaType0Type0.from_dict(data)

                return componentsschemas_honor_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_honor_section_meta_type_0_type_1 = HonorSectionMetaType0Type1.from_dict(data)

                return componentsschemas_honor_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_honor_section_meta_type_1 = HonorSectionMetaType1.from_dict(data)

                return componentsschemas_honor_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_honor_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_honor_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_honor_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

            return componentsschemas_honor_section_meta_type_3

        honors = _parse_honors(d.pop("honors"))

        def _parse_company_interests(
            data: object,
        ) -> (
            CompanyInterestSectionMetaType0Type0Type0
            | CompanyInterestSectionMetaType0Type0Type1
            | CompanyInterestSectionMetaType0Type1
            | FailedSectionMeta
            | NotRequestedSectionMeta
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_interest_section_meta_type_0_type_0_type_0 = (
                    CompanyInterestSectionMetaType0Type0Type0.from_dict(data)
                )

                return componentsschemas_company_interest_section_meta_type_0_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_interest_section_meta_type_0_type_0_type_1 = (
                    CompanyInterestSectionMetaType0Type0Type1.from_dict(data)
                )

                return componentsschemas_company_interest_section_meta_type_0_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_interest_section_meta_type_0_type_1 = (
                    CompanyInterestSectionMetaType0Type1.from_dict(data)
                )

                return componentsschemas_company_interest_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_interest_section_meta_type_0_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_company_interest_section_meta_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_interest_section_meta_type_0_type_3 = SkippedSectionMeta.from_dict(data)

                return componentsschemas_company_interest_section_meta_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_company_interest_section_meta_type_1 = NotRequestedSectionMeta.from_dict(data)

            return componentsschemas_company_interest_section_meta_type_1

        company_interests = _parse_company_interests(d.pop("companyInterests"))

        def _parse_contact(
            data: object,
        ) -> (
            ContactSectionMetaType0Type0
            | ContactSectionMetaType0Type1
            | ContactSectionMetaType1
            | FailedSectionMeta
            | NotRequestedSectionMeta
            | SkippedSectionMeta
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contact_section_meta_type_0_type_0 = ContactSectionMetaType0Type0.from_dict(data)

                return componentsschemas_contact_section_meta_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contact_section_meta_type_0_type_1 = ContactSectionMetaType0Type1.from_dict(data)

                return componentsschemas_contact_section_meta_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contact_section_meta_type_1 = ContactSectionMetaType1.from_dict(data)

                return componentsschemas_contact_section_meta_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contact_section_meta_type_2 = FailedSectionMeta.from_dict(data)

                return componentsschemas_contact_section_meta_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_contact_section_meta_type_3 = SkippedSectionMeta.from_dict(data)

                return componentsschemas_contact_section_meta_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_contact_section_meta_type_4 = NotRequestedSectionMeta.from_dict(data)

            return componentsschemas_contact_section_meta_type_4

        contact = _parse_contact(d.pop("contact"))

        profile_sections = cls(
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

        return profile_sections
