from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contact_website_category import ContactWebsiteCategory

T = TypeVar("T", bound="ContactWebsite")


@_attrs_define
class ContactWebsite:
    """
    Attributes:
        url (str):
        category (ContactWebsiteCategory | None):
        label (None | str):
    """

    url: str
    category: ContactWebsiteCategory | None
    label: None | str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        category: None | str
        if isinstance(self.category, ContactWebsiteCategory):
            category = self.category.value
        else:
            category = self.category

        label: None | str
        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "category": category,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_category(data: object) -> ContactWebsiteCategory | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = ContactWebsiteCategory(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactWebsiteCategory | None, data)

        category = _parse_category(d.pop("category"))

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        contact_website = cls(
            url=url,
            category=category,
            label=label,
        )

        return contact_website
