from enum import StrEnum


class OrganizationTypeCode(StrEnum):
    EDUCATIONAL = "educational"
    GOVERNMENTAGENCY = "governmentAgency"
    NONPROFIT = "nonProfit"
    PARTNERSHIP = "partnership"
    PRIVATELYHELD = "privatelyHeld"
    PUBLICCOMPANY = "publicCompany"
    SELFEMPLOYED = "selfEmployed"
    SELFOWNED = "selfOwned"

    def __str__(self) -> str:
        return str(self.value)
