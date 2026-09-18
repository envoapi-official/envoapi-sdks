from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_domain_search_data import CompanyDomainSearchData
    from ..models.company_keyword_search_success_meta import CompanyKeywordSearchSuccessMeta


T = TypeVar("T", bound="CompanyKeywordSearchSuccess")


@_attrs_define
class CompanyKeywordSearchSuccess:
    """
    Attributes:
        data (CompanyDomainSearchData):
        meta (CompanyKeywordSearchSuccessMeta):
    """

    data: CompanyDomainSearchData
    meta: CompanyKeywordSearchSuccessMeta

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_domain_search_data import CompanyDomainSearchData  # noqa: PLC0415
        from ..models.company_keyword_search_success_meta import CompanyKeywordSearchSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyDomainSearchData.from_dict(d.pop("data"))

        meta = CompanyKeywordSearchSuccessMeta.from_dict(d.pop("meta"))

        company_keyword_search_success = cls(
            data=data,
            meta=meta,
        )

        return company_keyword_search_success
