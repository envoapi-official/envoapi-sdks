from enum import StrEnum


class SearchJobsTimePosted(StrEnum):
    ANY = "any"
    DAY = "day"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
