from enum import StrEnum


class LinkedInV2PostCommentsQueryType0SortOrder(StrEnum):
    CHRONOLOGICAL = "CHRONOLOGICAL"
    RELEVANCE = "RELEVANCE"

    def __str__(self) -> str:
        return str(self.value)
