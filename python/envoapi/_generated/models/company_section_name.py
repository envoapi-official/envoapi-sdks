from enum import StrEnum


class CompanySectionName(StrEnum):
    COMPANY = "company"
    PRODUCTS = "products"

    def __str__(self) -> str:
        return str(self.value)
