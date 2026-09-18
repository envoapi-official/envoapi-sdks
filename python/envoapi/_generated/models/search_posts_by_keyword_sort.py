from enum import StrEnum


class SearchPostsByKeywordSort(StrEnum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
