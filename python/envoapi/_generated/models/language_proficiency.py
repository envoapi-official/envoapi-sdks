from enum import StrEnum


class LanguageProficiency(StrEnum):
    ELEMENTARY = "elementary"
    FULLPROFESSIONAL = "fullProfessional"
    LIMITEDWORKING = "limitedWorking"
    NATIVEORBILINGUAL = "nativeOrBilingual"
    PROFESSIONALWORKING = "professionalWorking"

    def __str__(self) -> str:
        return str(self.value)
