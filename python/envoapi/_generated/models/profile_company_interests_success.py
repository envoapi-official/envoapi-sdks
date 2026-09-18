from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_company_interests_data import ProfileCompanyInterestsData
    from ..models.profile_company_interests_success_meta import ProfileCompanyInterestsSuccessMeta


T = TypeVar("T", bound="ProfileCompanyInterestsSuccess")


@_attrs_define
class ProfileCompanyInterestsSuccess:
    """
    Attributes:
        data (ProfileCompanyInterestsData):
        meta (ProfileCompanyInterestsSuccessMeta):
    """

    data: ProfileCompanyInterestsData
    meta: ProfileCompanyInterestsSuccessMeta

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
        from ..models.profile_company_interests_data import ProfileCompanyInterestsData  # noqa: PLC0415
        from ..models.profile_company_interests_success_meta import ProfileCompanyInterestsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = ProfileCompanyInterestsData.from_dict(d.pop("data"))

        meta = ProfileCompanyInterestsSuccessMeta.from_dict(d.pop("meta"))

        profile_company_interests_success = cls(
            data=data,
            meta=meta,
        )

        return profile_company_interests_success
