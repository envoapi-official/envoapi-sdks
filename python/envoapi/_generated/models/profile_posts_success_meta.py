from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_posts_paging import ProfilePostsPaging


T = TypeVar("T", bound="ProfilePostsSuccessMeta")


@_attrs_define
class ProfilePostsSuccessMeta:
    """
    Attributes:
        credit_cost (int):
        paging (ProfilePostsPaging | Unset):
    """

    credit_cost: int
    paging: ProfilePostsPaging | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credit_cost = self.credit_cost

        paging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "creditCost": credit_cost,
            }
        )
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_posts_paging import ProfilePostsPaging  # noqa: PLC0415

        d = dict(src_dict)
        credit_cost = d.pop("creditCost")

        _paging = d.pop("paging", UNSET)
        paging: ProfilePostsPaging | Unset
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = ProfilePostsPaging.from_dict(_paging)

        profile_posts_success_meta = cls(
            credit_cost=credit_cost,
            paging=paging,
        )

        return profile_posts_success_meta
