from enum import StrEnum


class LinkedInV2ProfileDetailSection(StrEnum):
    CERTIFICATIONS = "certifications"
    COMPANY_INTERESTS = "company_interests"
    COURSES = "courses"
    EDUCATION = "education"
    HONORS = "honors"
    LANGUAGES = "languages"
    ORGANIZATIONS = "organizations"
    POSITIONS = "positions"
    SECTIONS = "sections"
    SKILLS = "skills"
    VOLUNTEER = "volunteer"

    def __str__(self) -> str:
        return str(self.value)
