from enum import StrEnum


class LinkedInV2CompanyProductsQueryState(StrEnum):
    PUBLISHED = "PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
