from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_skills_data import ProfileSkillsData
    from ..models.profile_skills_success_meta import ProfileSkillsSuccessMeta


T = TypeVar("T", bound="ProfileSkillsSuccess")


@_attrs_define
class ProfileSkillsSuccess:
    """
    Attributes:
        data (ProfileSkillsData):
        meta (ProfileSkillsSuccessMeta):
    """

    data: ProfileSkillsData
    meta: ProfileSkillsSuccessMeta

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
        from ..models.profile_skills_data import ProfileSkillsData  # noqa: PLC0415
        from ..models.profile_skills_success_meta import ProfileSkillsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileSkillsData.from_dict(d.pop("data"))

        meta = ProfileSkillsSuccessMeta.from_dict(d.pop("meta"))

        profile_skills_success = cls(
            data=data,
            meta=meta,
        )

        return profile_skills_success
