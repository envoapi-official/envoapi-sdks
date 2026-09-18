from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.lookup_service_unavailable_post_rate_response_headers import (
        LookupServiceUnavailablePostRateResponseHeaders,
    )
    from ..models.retryable_service_unavailable_error_response import RetryableServiceUnavailableErrorResponse


T = TypeVar("T", bound="LookupServiceUnavailableResponseType1")


@_attrs_define
class LookupServiceUnavailableResponseType1:
    """
    Attributes:
        body (RetryableServiceUnavailableErrorResponse):
        headers (LookupServiceUnavailablePostRateResponseHeaders):
    """

    body: RetryableServiceUnavailableErrorResponse
    headers: LookupServiceUnavailablePostRateResponseHeaders

    def to_dict(self) -> dict[str, Any]:
        body = self.body.to_dict()

        headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body": body,
                "headers": headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lookup_service_unavailable_post_rate_response_headers import (
            LookupServiceUnavailablePostRateResponseHeaders,  # noqa: PLC0415
        )
        from ..models.retryable_service_unavailable_error_response import (
            RetryableServiceUnavailableErrorResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        body = RetryableServiceUnavailableErrorResponse.from_dict(d.pop("body"))

        headers = LookupServiceUnavailablePostRateResponseHeaders.from_dict(d.pop("headers"))

        lookup_service_unavailable_response_type_1 = cls(
            body=body,
            headers=headers,
        )

        return lookup_service_unavailable_response_type_1
