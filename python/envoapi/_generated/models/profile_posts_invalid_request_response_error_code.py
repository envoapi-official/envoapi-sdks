from enum import StrEnum


class ProfilePostsInvalidRequestResponseErrorCode(StrEnum):
    CURSOR_EXPIRED = "cursor_expired"
    INVALID_CURSOR = "invalid_cursor"
    INVALID_REQUEST = "invalid_request"

    def __str__(self) -> str:
        return str(self.value)
