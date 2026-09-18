from enum import StrEnum


class ValidationDetailCode(StrEnum):
    IDENTIFIER_COUNT = "identifier_count"
    INVALID_FORMAT = "invalid_format"
    INVALID_VALUE = "invalid_value"
    REPEATED_PARAMETER = "repeated_parameter"
    TOO_LONG = "too_long"
    UNKNOWN_PARAMETER = "unknown_parameter"

    def __str__(self) -> str:
        return str(self.value)
