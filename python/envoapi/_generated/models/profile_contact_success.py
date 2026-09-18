from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.contact import Contact
    from ..models.profile_success_metadata import ProfileSuccessMetadata


T = TypeVar("T", bound="ProfileContactSuccess")


@_attrs_define
class ProfileContactSuccess:
    """
    Attributes:
        data (Contact):
        meta (ProfileSuccessMetadata):
    """

    data: Contact
    meta: ProfileSuccessMetadata

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact import Contact  # noqa: PLC0415
        from ..models.profile_success_metadata import ProfileSuccessMetadata  # noqa: PLC0415

        d = dict(src_dict)
        data = Contact.from_dict(d.pop("data"))

        meta = ProfileSuccessMetadata.from_dict(d.pop("meta"))

        profile_contact_success = cls(
            data=data,
            meta=meta,
        )

        return profile_contact_success
