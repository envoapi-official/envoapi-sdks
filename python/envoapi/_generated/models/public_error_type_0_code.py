from enum import StrEnum


class PublicErrorType0Code(StrEnum):
    INTERNAL_ERROR = "internal_error"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    UPSTREAM_ERROR = "upstream_error"
    UPSTREAM_TIMEOUT = "upstream_timeout"

    def __str__(self) -> str:
        return str(self.value)
