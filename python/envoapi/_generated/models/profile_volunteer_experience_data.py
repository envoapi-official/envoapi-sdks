from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.volunteer_experience_item import VolunteerExperienceItem


T = TypeVar("T", bound="ProfileVolunteerExperienceData")


@_attrs_define
class ProfileVolunteerExperienceData:
    """
    Attributes:
        volunteer_experience (list[VolunteerExperienceItem]):
    """

    volunteer_experience: list[VolunteerExperienceItem]

    def to_dict(self) -> dict[str, Any]:
        volunteer_experience = []
        for componentsschemas_volunteer_experience_list_item_data in self.volunteer_experience:
            componentsschemas_volunteer_experience_list_item = (
                componentsschemas_volunteer_experience_list_item_data.to_dict()
            )
            volunteer_experience.append(componentsschemas_volunteer_experience_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "volunteerExperience": volunteer_experience,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_experience_item import VolunteerExperienceItem  # noqa: PLC0415

        d = dict(src_dict)
        volunteer_experience = []
        _volunteer_experience = d.pop("volunteerExperience")
        for componentsschemas_volunteer_experience_list_item_data in _volunteer_experience:
            componentsschemas_volunteer_experience_list_item = VolunteerExperienceItem.from_dict(
                componentsschemas_volunteer_experience_list_item_data
            )

            volunteer_experience.append(componentsschemas_volunteer_experience_list_item)

        profile_volunteer_experience_data = cls(
            volunteer_experience=volunteer_experience,
        )

        return profile_volunteer_experience_data
