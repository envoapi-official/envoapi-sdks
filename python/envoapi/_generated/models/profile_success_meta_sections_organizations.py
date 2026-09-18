from enum import StrEnum


class ProfileSuccessMetaSectionsOrganizations(StrEnum):
    COMPLETE = "complete"
    EMPTY = "empty"
    INCOMPLETE = "incomplete"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
