from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_public_item_attributes_item_type_0 import LinkedInV2PublicItemAttributesItemType0
    from ..models.linked_in_v2_public_item_attributes_item_type_1 import LinkedInV2PublicItemAttributesItemType1
    from ..models.linked_in_v2_public_item_links_item import LinkedInV2PublicItemLinksItem


T = TypeVar("T", bound="LinkedInV2PublicItem")


@_attrs_define
class LinkedInV2PublicItem:
    """
    Attributes:
        attributes (list[LinkedInV2PublicItemAttributesItemType0 | LinkedInV2PublicItemAttributesItemType1]):
        links (list[LinkedInV2PublicItemLinksItem]):
    """

    attributes: list[LinkedInV2PublicItemAttributesItemType0 | LinkedInV2PublicItemAttributesItemType1]
    links: list[LinkedInV2PublicItemLinksItem]

    def to_dict(self) -> dict[str, Any]:
        from ..models.linked_in_v2_public_item_attributes_item_type_0 import (
            LinkedInV2PublicItemAttributesItemType0,  # noqa: PLC0415
        )

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item: dict[str, Any]
            if isinstance(attributes_item_data, LinkedInV2PublicItemAttributesItemType0):
                attributes_item = attributes_item_data.to_dict()
            else:
                attributes_item = attributes_item_data.to_dict()

            attributes.append(attributes_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linked_in_v2_public_item_attributes_item_type_0 import (
            LinkedInV2PublicItemAttributesItemType0,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_public_item_attributes_item_type_1 import (
            LinkedInV2PublicItemAttributesItemType1,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_public_item_links_item import LinkedInV2PublicItemLinksItem  # noqa: PLC0415

        d = dict(src_dict)
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:

            def _parse_attributes_item(
                data: object,
            ) -> LinkedInV2PublicItemAttributesItemType0 | LinkedInV2PublicItemAttributesItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    attributes_item_type_0 = LinkedInV2PublicItemAttributesItemType0.from_dict(data)

                    return attributes_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_item_type_1 = LinkedInV2PublicItemAttributesItemType1.from_dict(data)

                return attributes_item_type_1

            attributes_item = _parse_attributes_item(attributes_item_data)

            attributes.append(attributes_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkedInV2PublicItemLinksItem.from_dict(links_item_data)

            links.append(links_item)

        linked_in_v2_public_item = cls(
            attributes=attributes,
            links=links,
        )

        return linked_in_v2_public_item
