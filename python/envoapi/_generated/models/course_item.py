from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CourseItem")


@_attrs_define
class CourseItem:
    """
    Attributes:
        name (str):
        associated_with (None | str):
    """

    name: str
    associated_with: None | str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        associated_with: None | str
        associated_with = self.associated_with

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "associatedWith": associated_with,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_associated_with(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        associated_with = _parse_associated_with(d.pop("associatedWith"))

        course_item = cls(
            name=name,
            associated_with=associated_with,
        )

        return course_item
