from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.similar_companies_data import SimilarCompaniesData
    from ..models.similar_companies_success_meta import SimilarCompaniesSuccessMeta


T = TypeVar("T", bound="SimilarCompaniesSuccess")


@_attrs_define
class SimilarCompaniesSuccess:
    """
    Attributes:
        data (SimilarCompaniesData):
        meta (SimilarCompaniesSuccessMeta):
    """

    data: SimilarCompaniesData
    meta: SimilarCompaniesSuccessMeta

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
        from ..models.similar_companies_data import SimilarCompaniesData  # noqa: PLC0415
        from ..models.similar_companies_success_meta import SimilarCompaniesSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = SimilarCompaniesData.from_dict(d.pop("data"))

        meta = SimilarCompaniesSuccessMeta.from_dict(d.pop("meta"))

        similar_companies_success = cls(
            data=data,
            meta=meta,
        )

        return similar_companies_success
