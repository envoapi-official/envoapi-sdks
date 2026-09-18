from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_education_data import ProfileEducationData
    from ..models.profile_success_metadata import ProfileSuccessMetadata


T = TypeVar("T", bound="ProfileEducationSuccess")


@_attrs_define
class ProfileEducationSuccess:
    """
    Attributes:
        data (ProfileEducationData):
        meta (ProfileSuccessMetadata):
    """

    data: ProfileEducationData
    meta: ProfileSuccessMetadata

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
        from ..models.profile_education_data import ProfileEducationData  # noqa: PLC0415
        from ..models.profile_success_metadata import ProfileSuccessMetadata  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileEducationData.from_dict(d.pop("data"))

        meta = ProfileSuccessMetadata.from_dict(d.pop("meta"))

        profile_education_success = cls(
            data=data,
            meta=meta,
        )

        return profile_education_success
