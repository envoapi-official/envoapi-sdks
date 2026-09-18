from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.linked_in_v2_public_item_links_item_kind import LinkedInV2PublicItemLinksItemKind

T = TypeVar("T", bound="LinkedInV2PublicItemLinksItem")


@_attrs_define
class LinkedInV2PublicItemLinksItem:
    """
    Attributes:
        kind (LinkedInV2PublicItemLinksItemKind):
        url (str):
    """

    kind: LinkedInV2PublicItemLinksItemKind
    url: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = LinkedInV2PublicItemLinksItemKind(d.pop("kind"))

        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        linked_in_v2_public_item_links_item = cls(
            kind=kind,
            url=url,
        )

        return linked_in_v2_public_item_links_item
