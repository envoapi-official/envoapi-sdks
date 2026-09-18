from enum import StrEnum


class ProfileSectionName(StrEnum):
    CERTIFICATIONS = "certifications"
    COMPANYINTERESTS = "companyInterests"
    CONTACT = "contact"
    COUNTS = "counts"
    COURSES = "courses"
    EDUCATION = "education"
    HONORS = "honors"
    LANGUAGES = "languages"
    ORGANIZATIONS = "organizations"
    POSITIONS = "positions"
    PROFILE = "profile"
    SKILLS = "skills"
    VOLUNTEEREXPERIENCE = "volunteerExperience"

    def __str__(self) -> str:
        return str(self.value)
