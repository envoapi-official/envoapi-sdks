from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_certifications_data import ProfileCertificationsData
    from ..models.profile_success_metadata import ProfileSuccessMetadata


T = TypeVar("T", bound="ProfileCertificationsSuccess")


@_attrs_define
class ProfileCertificationsSuccess:
    """
    Attributes:
        data (ProfileCertificationsData):
        meta (ProfileSuccessMetadata):
    """

    data: ProfileCertificationsData
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
        from ..models.profile_certifications_data import ProfileCertificationsData  # noqa: PLC0415
        from ..models.profile_success_metadata import ProfileSuccessMetadata  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileCertificationsData.from_dict(d.pop("data"))

        meta = ProfileSuccessMetadata.from_dict(d.pop("meta"))

        profile_certifications_success = cls(
            data=data,
            meta=meta,
        )

        return profile_certifications_success
