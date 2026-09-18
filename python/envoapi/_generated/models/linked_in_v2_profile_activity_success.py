from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_profile_activity_success_data import LinkedInV2ProfileActivitySuccessData
    from ..models.linked_in_v2_profile_activity_success_meta import LinkedInV2ProfileActivitySuccessMeta


T = TypeVar("T", bound="LinkedInV2ProfileActivitySuccess")


@_attrs_define
class LinkedInV2ProfileActivitySuccess:
    """
    Attributes:
        data (LinkedInV2ProfileActivitySuccessData):
        meta (LinkedInV2ProfileActivitySuccessMeta):
    """

    data: LinkedInV2ProfileActivitySuccessData
    meta: LinkedInV2ProfileActivitySuccessMeta

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
        from ..models.linked_in_v2_profile_activity_success_data import (
            LinkedInV2ProfileActivitySuccessData,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_profile_activity_success_meta import (
            LinkedInV2ProfileActivitySuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LinkedInV2ProfileActivitySuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2ProfileActivitySuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_profile_activity_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_profile_activity_success
