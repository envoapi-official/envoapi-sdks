from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostReactorType1")


@_attrs_define
class PostReactorType1:
    """
    Attributes:
        kind (Literal['company']):
        name (str):
        headline (None | str):
        url (str):
        picture_url (None | str):
    """

    kind: Literal["company"]
    name: str
    headline: None | str
    url: str
    picture_url: None | str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        name = self.name

        headline: None | str
        headline = self.headline

        url = self.url

        picture_url: None | str
        picture_url = self.picture_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "headline": headline,
                "url": url,
                "pictureUrl": picture_url,
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

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        picture_url = _parse_picture_url(d.pop("pictureUrl"))

        post_reactor_type_1 = cls(
            kind=kind,
            name=name,
            headline=headline,
            url=url,
            picture_url=picture_url,
        )

        return post_reactor_type_1
