from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_success_meta_sections import ProfileSuccessMetaSections
    from ..models.profile_success_meta_skills import ProfileSuccessMetaSkills


T = TypeVar("T", bound="ProfileSuccessMeta")


@_attrs_define
class ProfileSuccessMeta:
    """
    Attributes:
        credit_cost (int):
        skills (ProfileSuccessMetaSkills):
        sections (ProfileSuccessMetaSections | Unset): Section availability: complete means fully observed, empty means
            confirmed empty, incomplete means only partial evidence, and unavailable means no usable evidence. Incomplete
            non-skills sections return null; skills may return a preview.
    """

    credit_cost: int
    skills: ProfileSuccessMetaSkills
    sections: ProfileSuccessMetaSections | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credit_cost = self.credit_cost

        skills = self.skills.to_dict()

        sections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "creditCost": credit_cost,
                "skills": skills,
            }
        )
        if sections is not UNSET:
            field_dict["sections"] = sections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_success_meta_sections import ProfileSuccessMetaSections  # noqa: PLC0415
        from ..models.profile_success_meta_skills import ProfileSuccessMetaSkills  # noqa: PLC0415

        d = dict(src_dict)
        credit_cost = d.pop("creditCost")

        skills = ProfileSuccessMetaSkills.from_dict(d.pop("skills"))

        _sections = d.pop("sections", UNSET)
        sections: ProfileSuccessMetaSections | Unset
        if isinstance(_sections, Unset):
            sections = UNSET
        else:
            sections = ProfileSuccessMetaSections.from_dict(_sections)

        profile_success_meta = cls(
            credit_cost=credit_cost,
            skills=skills,
            sections=sections,
        )

        return profile_success_meta
