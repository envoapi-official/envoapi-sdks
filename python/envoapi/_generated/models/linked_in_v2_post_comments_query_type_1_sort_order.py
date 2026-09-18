from enum import StrEnum


class LinkedInV2PostCommentsQueryType1SortOrder(StrEnum):
    CHRONOLOGICAL = "CHRONOLOGICAL"
    RELEVANCE = "RELEVANCE"

    def __str__(self) -> str:
        return str(self.value)
