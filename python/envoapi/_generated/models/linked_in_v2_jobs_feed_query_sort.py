from enum import StrEnum


class LinkedInV2JobsFeedQuerySort(StrEnum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
