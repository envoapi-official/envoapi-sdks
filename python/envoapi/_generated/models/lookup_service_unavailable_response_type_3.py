from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.lookup_settlement_uncertain_without_key_response_headers import (
        LookupSettlementUncertainWithoutKeyResponseHeaders,
    )
    from ..models.non_retryable_service_unavailable_error_response import NonRetryableServiceUnavailableErrorResponse


T = TypeVar("T", bound="LookupServiceUnavailableResponseType3")


@_attrs_define
class LookupServiceUnavailableResponseType3:
    """
    Attributes:
        body (NonRetryableServiceUnavailableErrorResponse):
        headers (LookupSettlementUncertainWithoutKeyResponseHeaders):
    """

    body: NonRetryableServiceUnavailableErrorResponse
    headers: LookupSettlementUncertainWithoutKeyResponseHeaders

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
        from ..models.lookup_settlement_uncertain_without_key_response_headers import (
            LookupSettlementUncertainWithoutKeyResponseHeaders,  # noqa: PLC0415
        )
        from ..models.non_retryable_service_unavailable_error_response import (
            NonRetryableServiceUnavailableErrorResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        body = NonRetryableServiceUnavailableErrorResponse.from_dict(d.pop("body"))

        headers = LookupSettlementUncertainWithoutKeyResponseHeaders.from_dict(d.pop("headers"))

        lookup_service_unavailable_response_type_3 = cls(
            body=body,
            headers=headers,
        )

        return lookup_service_unavailable_response_type_3
