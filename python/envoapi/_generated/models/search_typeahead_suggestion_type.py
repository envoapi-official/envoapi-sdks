from enum import StrEnum


class SearchTypeaheadSuggestionType(StrEnum):
    COMPANY = "company"
    ENTITY = "entity"
    EVENT = "event"
    GROUP = "group"
    JOB = "job"
    LOCATION = "location"
    PROFILE = "profile"
    QUERY = "query"
    SCHOOL = "school"

    def __str__(self) -> str:
        return str(self.value)
