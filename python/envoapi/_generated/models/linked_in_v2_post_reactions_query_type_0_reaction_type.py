from enum import StrEnum


class LinkedInV2PostReactionsQueryType0ReactionType(StrEnum):
    APPRECIATION = "APPRECIATION"
    EMPATHY = "EMPATHY"
    ENTERTAINMENT = "ENTERTAINMENT"
    INTEREST = "INTEREST"
    LIKE = "LIKE"
    PRAISE = "PRAISE"

    def __str__(self) -> str:
        return str(self.value)
