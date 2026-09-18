from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_details_data import CompanyDetailsData
    from ..models.company_success_metadata import CompanySuccessMetadata


T = TypeVar("T", bound="CompanySuccess")


@_attrs_define
class CompanySuccess:
    """
    Attributes:
        data (CompanyDetailsData):
        meta (CompanySuccessMetadata):
    """

    data: CompanyDetailsData
    meta: CompanySuccessMetadata

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
        from ..models.company_details_data import CompanyDetailsData  # noqa: PLC0415
        from ..models.company_success_metadata import CompanySuccessMetadata  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyDetailsData.from_dict(d.pop("data"))

        meta = CompanySuccessMetadata.from_dict(d.pop("meta"))

        company_success = cls(
            data=data,
            meta=meta,
        )

        return company_success
