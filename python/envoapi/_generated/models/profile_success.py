from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_details_data import ProfileDetailsData
    from ..models.profile_success_meta import ProfileSuccessMeta


T = TypeVar("T", bound="ProfileSuccess")


@_attrs_define
class ProfileSuccess:
    """
    Attributes:
        data (ProfileDetailsData):
        meta (ProfileSuccessMeta):
    """

    data: ProfileDetailsData
    meta: ProfileSuccessMeta

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
        from ..models.profile_details_data import ProfileDetailsData  # noqa: PLC0415
        from ..models.profile_success_meta import ProfileSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileDetailsData.from_dict(d.pop("data"))

        meta = ProfileSuccessMeta.from_dict(d.pop("meta"))

        profile_success = cls(
            data=data,
            meta=meta,
        )

        return profile_success
