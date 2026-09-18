from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_posts_data import ProfilePostsData
    from ..models.profile_posts_success_meta import ProfilePostsSuccessMeta


T = TypeVar("T", bound="ProfilePostsSuccess")


@_attrs_define
class ProfilePostsSuccess:
    """
    Attributes:
        data (ProfilePostsData):
        meta (ProfilePostsSuccessMeta):
    """

    data: ProfilePostsData
    meta: ProfilePostsSuccessMeta

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
        from ..models.profile_posts_data import ProfilePostsData  # noqa: PLC0415
        from ..models.profile_posts_success_meta import ProfilePostsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfilePostsData.from_dict(d.pop("data"))

        meta = ProfilePostsSuccessMeta.from_dict(d.pop("meta"))

        profile_posts_success = cls(
            data=data,
            meta=meta,
        )

        return profile_posts_success
