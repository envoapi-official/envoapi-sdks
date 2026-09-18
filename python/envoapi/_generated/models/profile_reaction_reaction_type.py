from enum import StrEnum


class ProfileReactionReactionType(StrEnum):
    APPRECIATION = "APPRECIATION"
    EMPATHY = "EMPATHY"
    ENTERTAINMENT = "ENTERTAINMENT"
    INTEREST = "INTEREST"
    LIKE = "LIKE"
    PRAISE = "PRAISE"

    def __str__(self) -> str:
        return str(self.value)
