from enum import StrEnum


class PublicErrorType1Code(StrEnum):
    ACCOUNT_SUSPENDED = "account_suspended"
    CURSOR_EXPIRED = "cursor_expired"
    IMAGE_NOT_FOUND = "image_not_found"
    INSUFFICIENT_CREDITS = "insufficient_credits"
    INSUFFICIENT_SCOPE = "insufficient_scope"
    INVALID_API_KEY = "invalid_api_key"
    INVALID_CURSOR = "invalid_cursor"
    INVALID_REQUEST = "invalid_request"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    NOT_ACCEPTABLE = "not_acceptable"
    RESOURCE_NOT_FOUND = "resource_not_found"
    RESPONSE_TOO_LARGE = "response_too_large"
    ROUTE_NOT_FOUND = "route_not_found"
    UNSUPPORTED_MEDIA_TYPE = "unsupported_media_type"

    def __str__(self) -> str:
        return str(self.value)
