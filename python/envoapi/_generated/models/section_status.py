from enum import StrEnum


class SectionStatus(StrEnum):
    COMPLETE = "complete"
    EMPTY = "empty"
    FAILED = "failed"
    NOTREQUESTED = "notRequested"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
