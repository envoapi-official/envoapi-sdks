from enum import StrEnum


class JobDetailsDataStatus(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
