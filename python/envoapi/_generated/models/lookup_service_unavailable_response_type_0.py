from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.lookup_service_unavailable_pre_rate_response_headers import (
        LookupServiceUnavailablePreRateResponseHeaders,
    )
    from ..models.retryable_service_unavailable_error_response import RetryableServiceUnavailableErrorResponse


T = TypeVar("T", bound="LookupServiceUnavailableResponseType0")


@_attrs_define
class LookupServiceUnavailableResponseType0:
    """
    Attributes:
        body (RetryableServiceUnavailableErrorResponse):
        headers (LookupServiceUnavailablePreRateResponseHeaders):
    """

    body: RetryableServiceUnavailableErrorResponse
    headers: LookupServiceUnavailablePreRateResponseHeaders

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
        from ..models.lookup_service_unavailable_pre_rate_response_headers import (
            LookupServiceUnavailablePreRateResponseHeaders,  # noqa: PLC0415
        )
        from ..models.retryable_service_unavailable_error_response import (
            RetryableServiceUnavailableErrorResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        body = RetryableServiceUnavailableErrorResponse.from_dict(d.pop("body"))

        headers = LookupServiceUnavailablePreRateResponseHeaders.from_dict(d.pop("headers"))

        lookup_service_unavailable_response_type_0 = cls(
            body=body,
            headers=headers,
        )

        return lookup_service_unavailable_response_type_0
