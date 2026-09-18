from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_profile_section_success_data import LinkedInV2ProfileSectionSuccessData
    from ..models.linked_in_v2_profile_section_success_meta import LinkedInV2ProfileSectionSuccessMeta


T = TypeVar("T", bound="LinkedInV2ProfileSectionSuccess")


@_attrs_define
class LinkedInV2ProfileSectionSuccess:
    """
    Attributes:
        data (LinkedInV2ProfileSectionSuccessData):
        meta (LinkedInV2ProfileSectionSuccessMeta):
    """

    data: LinkedInV2ProfileSectionSuccessData
    meta: LinkedInV2ProfileSectionSuccessMeta

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
        from ..models.linked_in_v2_profile_section_success_data import (
            LinkedInV2ProfileSectionSuccessData,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_profile_section_success_meta import (
            LinkedInV2ProfileSectionSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LinkedInV2ProfileSectionSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2ProfileSectionSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_profile_section_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_profile_section_success
