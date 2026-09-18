from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GetProfileSkillsByUsernameQuery")


@_attrs_define
class GetProfileSkillsByUsernameQuery:
    """
    Attributes:
        username (str):
        start (int):  Default: 0.
    """

    username: str
    start: int = 0

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "username": username,
                "start": start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")
        if not isinstance(username, str):
            raise TypeError("Expected string for username")

        start = d.pop("start")

        get_profile_skills_by_username_query = cls(
            username=username,
            start=start,
        )

        return get_profile_skills_by_username_query
