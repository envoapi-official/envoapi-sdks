from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileSkillsData")


@_attrs_define
class ProfileSkillsData:
    """
    Attributes:
        skills (list[str]):
    """

    skills: list[str]

    def to_dict(self) -> dict[str, Any]:
        skills = self.skills

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "skills": skills,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skills = cast(list[str], d.pop("skills"))

        profile_skills_data = cls(
            skills=skills,
        )

        return profile_skills_data
