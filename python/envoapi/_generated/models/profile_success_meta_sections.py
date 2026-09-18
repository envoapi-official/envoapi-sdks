from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.profile_success_meta_sections_certifications import ProfileSuccessMetaSectionsCertifications
from ..models.profile_success_meta_sections_counts import ProfileSuccessMetaSectionsCounts
from ..models.profile_success_meta_sections_courses import ProfileSuccessMetaSectionsCourses
from ..models.profile_success_meta_sections_education import ProfileSuccessMetaSectionsEducation
from ..models.profile_success_meta_sections_experience import ProfileSuccessMetaSectionsExperience
from ..models.profile_success_meta_sections_honors import ProfileSuccessMetaSectionsHonors
from ..models.profile_success_meta_sections_languages import ProfileSuccessMetaSectionsLanguages
from ..models.profile_success_meta_sections_organizations import ProfileSuccessMetaSectionsOrganizations
from ..models.profile_success_meta_sections_skills import ProfileSuccessMetaSectionsSkills
from ..models.profile_success_meta_sections_volunteer_experience import ProfileSuccessMetaSectionsVolunteerExperience

T = TypeVar("T", bound="ProfileSuccessMetaSections")


@_attrs_define
class ProfileSuccessMetaSections:
    """Section availability: complete means fully observed, empty means confirmed empty, incomplete means only partial
    evidence, and unavailable means no usable evidence. Incomplete non-skills sections return null; skills may return a
    preview.

        Attributes:
            counts (ProfileSuccessMetaSectionsCounts):
            experience (ProfileSuccessMetaSectionsExperience):
            education (ProfileSuccessMetaSectionsEducation):
            skills (ProfileSuccessMetaSectionsSkills):
            certifications (ProfileSuccessMetaSectionsCertifications):
            organizations (ProfileSuccessMetaSectionsOrganizations):
            languages (ProfileSuccessMetaSectionsLanguages):
            courses (ProfileSuccessMetaSectionsCourses):
            volunteer_experience (ProfileSuccessMetaSectionsVolunteerExperience):
            honors (ProfileSuccessMetaSectionsHonors):
    """

    counts: ProfileSuccessMetaSectionsCounts
    experience: ProfileSuccessMetaSectionsExperience
    education: ProfileSuccessMetaSectionsEducation
    skills: ProfileSuccessMetaSectionsSkills
    certifications: ProfileSuccessMetaSectionsCertifications
    organizations: ProfileSuccessMetaSectionsOrganizations
    languages: ProfileSuccessMetaSectionsLanguages
    courses: ProfileSuccessMetaSectionsCourses
    volunteer_experience: ProfileSuccessMetaSectionsVolunteerExperience
    honors: ProfileSuccessMetaSectionsHonors

    def to_dict(self) -> dict[str, Any]:
        counts = self.counts.value

        experience = self.experience.value

        education = self.education.value

        skills = self.skills.value

        certifications = self.certifications.value

        organizations = self.organizations.value

        languages = self.languages.value

        courses = self.courses.value

        volunteer_experience = self.volunteer_experience.value

        honors = self.honors.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
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
        d = dict(src_dict)
        counts = ProfileSuccessMetaSectionsCounts(d.pop("counts"))

        experience = ProfileSuccessMetaSectionsExperience(d.pop("experience"))

        education = ProfileSuccessMetaSectionsEducation(d.pop("education"))

        skills = ProfileSuccessMetaSectionsSkills(d.pop("skills"))

        certifications = ProfileSuccessMetaSectionsCertifications(d.pop("certifications"))

        organizations = ProfileSuccessMetaSectionsOrganizations(d.pop("organizations"))

        languages = ProfileSuccessMetaSectionsLanguages(d.pop("languages"))

        courses = ProfileSuccessMetaSectionsCourses(d.pop("courses"))

        volunteer_experience = ProfileSuccessMetaSectionsVolunteerExperience(d.pop("volunteerExperience"))

        honors = ProfileSuccessMetaSectionsHonors(d.pop("honors"))

        profile_success_meta_sections = cls(
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

        return profile_success_meta_sections
