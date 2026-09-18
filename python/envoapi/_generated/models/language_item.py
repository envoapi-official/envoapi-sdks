from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.language_proficiency import LanguageProficiency

T = TypeVar("T", bound="LanguageItem")


@_attrs_define
class LanguageItem:
    """
    Attributes:
        name (str):
        proficiency (LanguageProficiency | None):
    """

    name: str
    proficiency: LanguageProficiency | None

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        proficiency: None | str
        if isinstance(self.proficiency, LanguageProficiency):
            proficiency = self.proficiency.value
        else:
            proficiency = self.proficiency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "proficiency": proficiency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_proficiency(data: object) -> LanguageProficiency | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proficiency_type_0 = LanguageProficiency(data)

                return proficiency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LanguageProficiency | None, data)

        proficiency = _parse_proficiency(d.pop("proficiency"))

        language_item = cls(
            name=name,
            proficiency=proficiency,
        )

        return language_item
