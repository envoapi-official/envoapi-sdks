from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_reactions_data import ProfileReactionsData
    from ..models.profile_reactions_success_meta import ProfileReactionsSuccessMeta


T = TypeVar("T", bound="ProfileReactionsSuccess")


@_attrs_define
class ProfileReactionsSuccess:
    """
    Attributes:
        data (ProfileReactionsData):
        meta (ProfileReactionsSuccessMeta):
    """

    data: ProfileReactionsData
    meta: ProfileReactionsSuccessMeta

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
        from ..models.profile_reactions_data import ProfileReactionsData  # noqa: PLC0415
        from ..models.profile_reactions_success_meta import ProfileReactionsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileReactionsData.from_dict(d.pop("data"))

        meta = ProfileReactionsSuccessMeta.from_dict(d.pop("meta"))

        profile_reactions_success = cls(
            data=data,
            meta=meta,
        )

        return profile_reactions_success
