from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.search_posts_paging import SearchPostsPaging


T = TypeVar("T", bound="LinkedInV2SearchPostsSuccessMeta")


@_attrs_define
class LinkedInV2SearchPostsSuccessMeta:
    """
    Attributes:
        paging (SearchPostsPaging):
        credit_cost (int):
    """

    paging: SearchPostsPaging
    credit_cost: int

    def to_dict(self) -> dict[str, Any]:
        paging = self.paging.to_dict()

        credit_cost = self.credit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "paging": paging,
                "creditCost": credit_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_posts_paging import SearchPostsPaging  # noqa: PLC0415

        d = dict(src_dict)
        paging = SearchPostsPaging.from_dict(d.pop("paging"))

        credit_cost = d.pop("creditCost")

        linked_in_v2_search_posts_success_meta = cls(
            paging=paging,
            credit_cost=credit_cost,
        )

        return linked_in_v2_search_posts_success_meta
