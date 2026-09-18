from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.industry_search_industry import IndustrySearchIndustry


T = TypeVar("T", bound="IndustrySearchData")


@_attrs_define
class IndustrySearchData:
    """
    Attributes:
        industries (list[IndustrySearchIndustry]):
    """

    industries: list[IndustrySearchIndustry]

    def to_dict(self) -> dict[str, Any]:
        industries = []
        for industries_item_data in self.industries:
            industries_item = industries_item_data.to_dict()
            industries.append(industries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "industries": industries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.industry_search_industry import IndustrySearchIndustry  # noqa: PLC0415

        d = dict(src_dict)
        industries = []
        _industries = d.pop("industries")
        for industries_item_data in _industries:
            industries_item = IndustrySearchIndustry.from_dict(industries_item_data)

            industries.append(industries_item)

        industry_search_data = cls(
            industries=industries,
        )

        return industry_search_data
