from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_feature_success_data import LinkedInV2FeatureSuccessData
    from ..models.linked_in_v2_feature_success_meta import LinkedInV2FeatureSuccessMeta


T = TypeVar("T", bound="LinkedInV2FeatureSuccess")


@_attrs_define
class LinkedInV2FeatureSuccess:
    """
    Attributes:
        data (LinkedInV2FeatureSuccessData):
        meta (LinkedInV2FeatureSuccessMeta):
    """

    data: LinkedInV2FeatureSuccessData
    meta: LinkedInV2FeatureSuccessMeta

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
        from ..models.linked_in_v2_feature_success_data import LinkedInV2FeatureSuccessData  # noqa: PLC0415
        from ..models.linked_in_v2_feature_success_meta import LinkedInV2FeatureSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = LinkedInV2FeatureSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2FeatureSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_feature_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_feature_success
