from enum import StrEnum


class SearchPostsByKeywordQuerySort(StrEnum):
    RECENT = "recent"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
