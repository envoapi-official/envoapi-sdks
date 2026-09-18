from enum import StrEnum


class LinkedInV2JobSearchQuerySort(StrEnum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
