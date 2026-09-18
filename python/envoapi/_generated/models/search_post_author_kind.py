from enum import StrEnum


class SearchPostAuthorKind(StrEnum):
    COMPANY = "company"
    PROFILE = "profile"

    def __str__(self) -> str:
        return str(self.value)
