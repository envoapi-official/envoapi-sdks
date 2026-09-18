from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_success_metadata import ProfileSuccessMetadata
    from ..models.profile_volunteer_experience_data import ProfileVolunteerExperienceData


T = TypeVar("T", bound="ProfileVolunteerExperienceSuccess")


@_attrs_define
class ProfileVolunteerExperienceSuccess:
    """
    Attributes:
        data (ProfileVolunteerExperienceData):
        meta (ProfileSuccessMetadata):
    """

    data: ProfileVolunteerExperienceData
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
        from ..models.profile_success_metadata import ProfileSuccessMetadata  # noqa: PLC0415
        from ..models.profile_volunteer_experience_data import ProfileVolunteerExperienceData  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileVolunteerExperienceData.from_dict(d.pop("data"))

        meta = ProfileSuccessMetadata.from_dict(d.pop("meta"))

        profile_volunteer_experience_success = cls(
            data=data,
            meta=meta,
        )

        return profile_volunteer_experience_success
