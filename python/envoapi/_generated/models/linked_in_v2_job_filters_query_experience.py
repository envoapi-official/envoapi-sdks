from enum import StrEnum


class LinkedInV2JobFiltersQueryExperience(StrEnum):
    ASSOCIATE = "associate"
    DIRECTOR = "director"
    ENTRY = "entry"
    EXECUTIVE = "executive"
    INTERNSHIP = "internship"
    MID_SENIOR = "mid_senior"

    def __str__(self) -> str:
        return str(self.value)
