from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompanyPostAuthorType0")


@_attrs_define
class CompanyPostAuthorType0:
    """
    Attributes:
        kind (Literal['company']):
        name (str):
        url (str):
    """

    kind: Literal["company"]
    name: str
    url: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = cast(Literal["company"], d.pop("kind"))
        if kind != "company":
            raise ValueError(f"kind must match const 'company', got '{kind}'")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        company_post_author_type_0 = cls(
            kind=kind,
            name=name,
            url=url,
        )

        return company_post_author_type_0
