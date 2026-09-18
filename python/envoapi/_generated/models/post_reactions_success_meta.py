from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_reactions_paging import PostReactionsPaging


T = TypeVar("T", bound="PostReactionsSuccessMeta")


@_attrs_define
class PostReactionsSuccessMeta:
    """
    Attributes:
        paging (PostReactionsPaging):
        credit_cost (int):
    """

    paging: PostReactionsPaging
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
        from ..models.post_reactions_paging import PostReactionsPaging  # noqa: PLC0415

        d = dict(src_dict)
        paging = PostReactionsPaging.from_dict(d.pop("paging"))

        credit_cost = d.pop("creditCost")

        post_reactions_success_meta = cls(
            paging=paging,
            credit_cost=credit_cost,
        )

        return post_reactions_success_meta
