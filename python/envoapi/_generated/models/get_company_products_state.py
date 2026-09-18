from enum import StrEnum


class GetCompanyProductsState(StrEnum):
    PUBLISHED = "PUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
