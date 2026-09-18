from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.education_item import EducationItem


T = TypeVar("T", bound="ProfileEducationData")


@_attrs_define
class ProfileEducationData:
    """
    Attributes:
        education (list[EducationItem]):
    """

    education: list[EducationItem]

    def to_dict(self) -> dict[str, Any]:
        education = []
        for componentsschemas_education_list_item_data in self.education:
            componentsschemas_education_list_item = componentsschemas_education_list_item_data.to_dict()
            education.append(componentsschemas_education_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "education": education,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.education_item import EducationItem  # noqa: PLC0415

        d = dict(src_dict)
        education = []
        _education = d.pop("education")
        for componentsschemas_education_list_item_data in _education:
            componentsschemas_education_list_item = EducationItem.from_dict(componentsschemas_education_list_item_data)

            education.append(componentsschemas_education_list_item)

        profile_education_data = cls(
            education=education,
        )

        return profile_education_data
