from enum import StrEnum


class LinkedInV2ProfileSectionQuerySection(StrEnum):
    EDUCATION = "education"
    EXPERIENCE = "experience"
    SKILLS = "skills"

    def __str__(self) -> str:
        return str(self.value)
