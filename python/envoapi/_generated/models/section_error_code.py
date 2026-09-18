from enum import StrEnum


class SectionErrorCode(StrEnum):
    DEPENDENCYMISSING = "dependencyMissing"
    INTERNALERROR = "internalError"
    RATELIMITED = "rateLimited"
    UPSTREAMPARSEERROR = "upstreamParseError"
    UPSTREAMTIMEOUT = "upstreamTimeout"
    UPSTREAMUNAVAILABLE = "upstreamUnavailable"

    def __str__(self) -> str:
        return str(self.value)
