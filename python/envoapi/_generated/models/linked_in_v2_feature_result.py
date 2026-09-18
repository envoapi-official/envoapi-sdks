from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_public_item import LinkedInV2PublicItem


T = TypeVar("T", bound="LinkedInV2FeatureResult")


@_attrs_define
class LinkedInV2FeatureResult:
    """
    Attributes:
        items (list[LinkedInV2PublicItem]):
        count (int):
    """

    items: list[LinkedInV2PublicItem]
    count: int

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_in_v2_public_item import LinkedInV2PublicItem  # noqa: PLC0415

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = LinkedInV2PublicItem.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count")

        linked_in_v2_feature_result = cls(
            items=items,
            count=count,
        )

        return linked_in_v2_feature_result
