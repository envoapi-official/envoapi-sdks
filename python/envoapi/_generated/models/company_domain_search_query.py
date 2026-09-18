from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyDomainSearchQuery")


@_attrs_define
class CompanyDomainSearchQuery:
    """
    Attributes:
        domain (str):
        offset (int):  Default: 0.
    """

    domain: str
    offset: int = 0

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "domain": domain,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")
        if not isinstance(domain, str):
            raise TypeError("Expected string for domain")

        offset = d.pop("offset")

        company_domain_search_query = cls(
            domain=domain,
            offset=offset,
        )

        return company_domain_search_query
