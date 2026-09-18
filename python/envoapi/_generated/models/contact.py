from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.birth_date_type_0 import BirthDateType0
    from ..models.birth_date_type_1 import BirthDateType1
    from ..models.contact_phone import ContactPhone
    from ..models.contact_website import ContactWebsite
    from ..models.social_handle import SocialHandle


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        email_address (None | str):
        phone_numbers (list[ContactPhone] | None):
        websites (list[ContactWebsite] | None):
        social_handles (list[SocialHandle] | None):
        birthdate (BirthDateType0 | BirthDateType1 | None):
        address (None | str):
    """

    email_address: None | str
    phone_numbers: list[ContactPhone] | None
    websites: list[ContactWebsite] | None
    social_handles: list[SocialHandle] | None
    birthdate: BirthDateType0 | BirthDateType1 | None
    address: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.birth_date_type_0 import BirthDateType0  # noqa: PLC0415
        from ..models.birth_date_type_1 import BirthDateType1  # noqa: PLC0415

        email_address: None | str
        email_address = self.email_address

        phone_numbers: list[dict[str, Any]] | None
        if isinstance(self.phone_numbers, list):
            phone_numbers = []
            for phone_numbers_type_0_item_data in self.phone_numbers:
                phone_numbers_type_0_item = phone_numbers_type_0_item_data.to_dict()
                phone_numbers.append(phone_numbers_type_0_item)

        else:
            phone_numbers = self.phone_numbers

        websites: list[dict[str, Any]] | None
        if isinstance(self.websites, list):
            websites = []
            for websites_type_0_item_data in self.websites:
                websites_type_0_item = websites_type_0_item_data.to_dict()
                websites.append(websites_type_0_item)

        else:
            websites = self.websites

        social_handles: list[dict[str, Any]] | None
        if isinstance(self.social_handles, list):
            social_handles = []
            for social_handles_type_0_item_data in self.social_handles:
                social_handles_type_0_item = social_handles_type_0_item_data.to_dict()
                social_handles.append(social_handles_type_0_item)

        else:
            social_handles = self.social_handles

        birthdate: dict[str, Any] | None
        if isinstance(self.birthdate, BirthDateType0):
            birthdate = self.birthdate.to_dict()
        elif isinstance(self.birthdate, BirthDateType1):
            birthdate = self.birthdate.to_dict()
        else:
            birthdate = self.birthdate

        address: None | str
        address = self.address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "emailAddress": email_address,
                "phoneNumbers": phone_numbers,
                "websites": websites,
                "socialHandles": social_handles,
                "birthdate": birthdate,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.birth_date_type_0 import BirthDateType0  # noqa: PLC0415
        from ..models.birth_date_type_1 import BirthDateType1  # noqa: PLC0415
        from ..models.contact_phone import ContactPhone  # noqa: PLC0415
        from ..models.contact_website import ContactWebsite  # noqa: PLC0415
        from ..models.social_handle import SocialHandle  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_email_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_address = _parse_email_address(d.pop("emailAddress"))

        def _parse_phone_numbers(data: object) -> list[ContactPhone] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = []
                _phone_numbers_type_0 = data
                for phone_numbers_type_0_item_data in _phone_numbers_type_0:
                    phone_numbers_type_0_item = ContactPhone.from_dict(phone_numbers_type_0_item_data)

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactPhone] | None, data)

        phone_numbers = _parse_phone_numbers(d.pop("phoneNumbers"))

        def _parse_websites(data: object) -> list[ContactWebsite] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                websites_type_0 = []
                _websites_type_0 = data
                for websites_type_0_item_data in _websites_type_0:
                    websites_type_0_item = ContactWebsite.from_dict(websites_type_0_item_data)

                    websites_type_0.append(websites_type_0_item)

                return websites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContactWebsite] | None, data)

        websites = _parse_websites(d.pop("websites"))

        def _parse_social_handles(data: object) -> list[SocialHandle] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                social_handles_type_0 = []
                _social_handles_type_0 = data
                for social_handles_type_0_item_data in _social_handles_type_0:
                    social_handles_type_0_item = SocialHandle.from_dict(social_handles_type_0_item_data)

                    social_handles_type_0.append(social_handles_type_0_item)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SocialHandle] | None, data)

        social_handles = _parse_social_handles(d.pop("socialHandles"))

        def _parse_birthdate(data: object) -> BirthDateType0 | BirthDateType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_birth_date_type_0 = BirthDateType0.from_dict(data)

                return componentsschemas_birth_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_birth_date_type_1 = BirthDateType1.from_dict(data)

                return componentsschemas_birth_date_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BirthDateType0 | BirthDateType1 | None, data)

        birthdate = _parse_birthdate(d.pop("birthdate"))

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))

        contact = cls(
            email_address=email_address,
            phone_numbers=phone_numbers,
            websites=websites,
            social_handles=social_handles,
            birthdate=birthdate,
            address=address,
        )

        return contact
