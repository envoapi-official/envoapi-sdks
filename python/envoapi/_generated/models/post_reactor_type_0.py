from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="PostReactorType0")


@_attrs_define
class PostReactorType0:
    """
    Attributes:
        kind (Literal['profile']):
        public_id (None | str): Permanent Envo Profile ID when source identity is known; null for a username-only
            mention.
        name (str):
        headline (None | str):
        url (None | str): Public LinkedIn username URL, or null when the username is unknown.
        picture_url (None | str):
    """

    kind: Literal["profile"]
    public_id: None | str
    name: str
    headline: None | str
    url: None | str
    picture_url: None | str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        public_id: None | str
        public_id = self.public_id

        name = self.name

        headline: None | str
        headline = self.headline

        url: None | str
        url = self.url

        picture_url: None | str
        picture_url = self.picture_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "publicId": public_id,
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
        kind = cast(Literal["profile"], d.pop("kind"))
        if kind != "profile":
            raise ValueError(f"kind must match const 'profile', got '{kind}'")

        def _parse_public_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_id = _parse_public_id(d.pop("publicId"))

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        picture_url = _parse_picture_url(d.pop("pictureUrl"))

        post_reactor_type_0 = cls(
            kind=kind,
            public_id=public_id,
            name=name,
            headline=headline,
            url=url,
            picture_url=picture_url,
        )

        return post_reactor_type_0
