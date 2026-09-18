from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="Locale")


@_attrs_define
class Locale:
    """
    Attributes:
        language (str):
        country (None | str):
        script (None | str):
        variant (None | str):
    """

    language: str
    country: None | str
    script: None | str
    variant: None | str

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        country: None | str
        country = self.country

        script: None | str
        script = self.script

        variant: None | str
        variant = self.variant

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "language": language,
                "country": country,
                "script": script,
                "variant": variant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")
        if not isinstance(language, str):
            raise TypeError("Expected string for language")

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_script(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        script = _parse_script(d.pop("script"))

        def _parse_variant(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant = _parse_variant(d.pop("variant"))

        locale = cls(
            language=language,
            country=country,
            script=script,
            variant=variant,
        )

        return locale
