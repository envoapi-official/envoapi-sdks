from enum import StrEnum


class GetPostCommentsByUrlQuerySortOrder(StrEnum):
    CHRONOLOGICAL = "CHRONOLOGICAL"
    RELEVANCE = "RELEVANCE"

    def __str__(self) -> str:
        return str(self.value)
