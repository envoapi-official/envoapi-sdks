from enum import StrEnum


class EmploymentTypeCode(StrEnum):
    APPRENTICESHIP = "apprenticeship"
    CONTRACT = "contract"
    FREELANCE = "freelance"
    FULLTIME = "fullTime"
    INTERNSHIP = "internship"
    PARTTIME = "partTime"
    SEASONAL = "seasonal"
    SELFEMPLOYED = "selfEmployed"

    def __str__(self) -> str:
        return str(self.value)
