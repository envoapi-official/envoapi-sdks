from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_feature_result import LinkedInV2FeatureResult


T = TypeVar("T", bound="LinkedInV2ProfileActivitySuccessData")


@_attrs_define
class LinkedInV2ProfileActivitySuccessData:
    """
    Attributes:
        feature (Literal['profileActivity']):
        result (LinkedInV2FeatureResult):
    """

    feature: Literal["profileActivity"]
    result: LinkedInV2FeatureResult

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        result = self.result.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "feature": feature,
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_in_v2_feature_result import LinkedInV2FeatureResult  # noqa: PLC0415

        d = dict(src_dict)
        feature = cast(Literal["profileActivity"], d.pop("feature"))
        if feature != "profileActivity":
            raise ValueError(f"feature must match const 'profileActivity', got '{feature}'")

        result = LinkedInV2FeatureResult.from_dict(d.pop("result"))

        linked_in_v2_profile_activity_success_data = cls(
            feature=feature,
            result=result,
        )

        return linked_in_v2_profile_activity_success_data
