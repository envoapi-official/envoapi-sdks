from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0
    from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1


T = TypeVar("T", bound="ProfileCertificationsData")


@_attrs_define
class ProfileCertificationsData:
    """
    Attributes:
        certifications (list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1]):
    """

    certifications: list[Any | ProfileCertificationItemType0 | ProfileCertificationItemType1]

    def to_dict(self) -> dict[str, Any]:
        from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0  # noqa: PLC0415
        from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1  # noqa: PLC0415

        certifications = []
        for componentsschemas_profile_certification_list_item_data in self.certifications:
            componentsschemas_profile_certification_list_item: Any | dict[str, Any]
            if isinstance(componentsschemas_profile_certification_list_item_data, ProfileCertificationItemType0):
                componentsschemas_profile_certification_list_item = (
                    componentsschemas_profile_certification_list_item_data.to_dict()
                )
            elif isinstance(componentsschemas_profile_certification_list_item_data, ProfileCertificationItemType1):
                componentsschemas_profile_certification_list_item = (
                    componentsschemas_profile_certification_list_item_data.to_dict()
                )
            else:
                componentsschemas_profile_certification_list_item = (
                    componentsschemas_profile_certification_list_item_data
                )
            certifications.append(componentsschemas_profile_certification_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "certifications": certifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_certification_item_type_0 import ProfileCertificationItemType0  # noqa: PLC0415
        from ..models.profile_certification_item_type_1 import ProfileCertificationItemType1  # noqa: PLC0415

        d = dict(src_dict)
        certifications = []
        _certifications = d.pop("certifications")
        for componentsschemas_profile_certification_list_item_data in _certifications:

            def _parse_componentsschemas_profile_certification_list_item(
                data: object,
            ) -> Any | ProfileCertificationItemType0 | ProfileCertificationItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_profile_certification_item_type_0 = ProfileCertificationItemType0.from_dict(data)

                    return componentsschemas_profile_certification_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_profile_certification_item_type_1 = ProfileCertificationItemType1.from_dict(data)

                    return componentsschemas_profile_certification_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(Any | ProfileCertificationItemType0 | ProfileCertificationItemType1, data)

            componentsschemas_profile_certification_list_item = (
                _parse_componentsschemas_profile_certification_list_item(
                    componentsschemas_profile_certification_list_item_data
                )
            )

            certifications.append(componentsschemas_profile_certification_list_item)

        profile_certifications_data = cls(
            certifications=certifications,
        )

        return profile_certifications_data
