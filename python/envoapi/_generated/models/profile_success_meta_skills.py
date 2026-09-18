from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileSuccessMetaSkills")


@_attrs_define
class ProfileSuccessMetaSkills:
    """
    Attributes:
        has_more (bool | None): True when another skills page is confirmed, false when complete, null when completeness
            is unknown. Page through Get Profile Skills for the complete list.
    """

    has_more: bool | None

    def to_dict(self) -> dict[str, Any]:
        has_more: bool | None
        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_has_more(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        has_more = _parse_has_more(d.pop("hasMore"))

        profile_success_meta_skills = cls(
            has_more=has_more,
        )

        return profile_success_meta_skills
