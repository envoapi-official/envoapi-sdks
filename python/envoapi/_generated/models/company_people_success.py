from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_people_data import CompanyPeopleData
    from ..models.company_people_success_meta import CompanyPeopleSuccessMeta


T = TypeVar("T", bound="CompanyPeopleSuccess")


@_attrs_define
class CompanyPeopleSuccess:
    """
    Attributes:
        data (CompanyPeopleData):
        meta (CompanyPeopleSuccessMeta):
    """

    data: CompanyPeopleData
    meta: CompanyPeopleSuccessMeta

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
        from ..models.company_people_data import CompanyPeopleData  # noqa: PLC0415
        from ..models.company_people_success_meta import CompanyPeopleSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyPeopleData.from_dict(d.pop("data"))

        meta = CompanyPeopleSuccessMeta.from_dict(d.pop("meta"))

        company_people_success = cls(
            data=data,
            meta=meta,
        )

        return company_people_success
