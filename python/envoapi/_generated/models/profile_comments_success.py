from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_comments_data import ProfileCommentsData
    from ..models.profile_comments_success_meta import ProfileCommentsSuccessMeta


T = TypeVar("T", bound="ProfileCommentsSuccess")


@_attrs_define
class ProfileCommentsSuccess:
    """
    Attributes:
        data (ProfileCommentsData):
        meta (ProfileCommentsSuccessMeta):
    """

    data: ProfileCommentsData
    meta: ProfileCommentsSuccessMeta

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
        from ..models.profile_comments_data import ProfileCommentsData  # noqa: PLC0415
        from ..models.profile_comments_success_meta import ProfileCommentsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileCommentsData.from_dict(d.pop("data"))

        meta = ProfileCommentsSuccessMeta.from_dict(d.pop("meta"))

        profile_comments_success = cls(
            data=data,
            meta=meta,
        )

        return profile_comments_success
