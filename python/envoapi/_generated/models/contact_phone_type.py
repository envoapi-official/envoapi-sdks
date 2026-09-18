from enum import StrEnum


class ContactPhoneType(StrEnum):
    HOME = "home"
    MOBILE = "mobile"
    OTHER = "other"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
