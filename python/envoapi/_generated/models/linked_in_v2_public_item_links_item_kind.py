from enum import StrEnum


class LinkedInV2PublicItemLinksItemKind(StrEnum):
    COMPANY = "company"
    JOB = "job"
    POST = "post"
    PROFILE = "profile"
    SCHOOL = "school"

    def __str__(self) -> str:
        return str(self.value)
