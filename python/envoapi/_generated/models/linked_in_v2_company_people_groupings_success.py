from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_company_people_groupings_success_data import LinkedInV2CompanyPeopleGroupingsSuccessData
    from ..models.linked_in_v2_company_people_groupings_success_meta import LinkedInV2CompanyPeopleGroupingsSuccessMeta


T = TypeVar("T", bound="LinkedInV2CompanyPeopleGroupingsSuccess")


@_attrs_define
class LinkedInV2CompanyPeopleGroupingsSuccess:
    """
    Attributes:
        data (LinkedInV2CompanyPeopleGroupingsSuccessData):
        meta (LinkedInV2CompanyPeopleGroupingsSuccessMeta):
    """

    data: LinkedInV2CompanyPeopleGroupingsSuccessData
    meta: LinkedInV2CompanyPeopleGroupingsSuccessMeta

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
        from ..models.linked_in_v2_company_people_groupings_success_data import (
            LinkedInV2CompanyPeopleGroupingsSuccessData,  # noqa: PLC0415
        )
        from ..models.linked_in_v2_company_people_groupings_success_meta import (
            LinkedInV2CompanyPeopleGroupingsSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = LinkedInV2CompanyPeopleGroupingsSuccessData.from_dict(d.pop("data"))

        meta = LinkedInV2CompanyPeopleGroupingsSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_company_people_groupings_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_company_people_groupings_success
