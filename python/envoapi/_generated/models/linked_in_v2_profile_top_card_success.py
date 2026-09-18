from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_profile_top_card_success_data import LinkedInV2ProfileTopCardSuccessData
    from ..models.linked_in_v2_profile_top_card_success_meta import LinkedInV2ProfileTopCardSuccessMeta


T = TypeVar("T", bound="LinkedInV2ProfileTopCardSuccess")


@_attrs_define
class LinkedInV2ProfileTopCardSuccess:
    """
    Attributes:
        data (LinkedInV2ProfileTopCardSuccessData):
        meta (LinkedInV2ProfileTopCardSuccessMeta):
    """

    data: LinkedInV2ProfileTopCardSuccessData
    meta: LinkedInV2ProfileTopCardSuccessMeta

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
        from ..models.linked_in_v2_profile_top_card_success_data import (
            LinkedInV2ProfileTopCardSuccessData,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_profile_top_card_success_meta import (
            LinkedInV2ProfileTopCardSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LinkedInV2ProfileTopCardSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2ProfileTopCardSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_profile_top_card_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_profile_top_card_success
