from enum import StrEnum


class LinkedInV2SearchFiltersQueryResultType(StrEnum):
    COMPANIES = "COMPANIES"
    EVENTS = "EVENTS"
    GROUPS = "GROUPS"
    JOBS = "JOBS"
    PEOPLE = "PEOPLE"
    POSTS = "POSTS"
    SCHOOLS = "SCHOOLS"

    def __str__(self) -> str:
        return str(self.value)
