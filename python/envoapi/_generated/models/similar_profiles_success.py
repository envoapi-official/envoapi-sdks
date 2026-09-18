from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.similar_profiles_data import SimilarProfilesData
    from ..models.similar_profiles_success_meta import SimilarProfilesSuccessMeta


T = TypeVar("T", bound="SimilarProfilesSuccess")


@_attrs_define
class SimilarProfilesSuccess:
    """
    Attributes:
        data (SimilarProfilesData):
        meta (SimilarProfilesSuccessMeta):
    """

    data: SimilarProfilesData
    meta: SimilarProfilesSuccessMeta

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
        from ..models.similar_profiles_data import SimilarProfilesData  # noqa: PLC0415
        from ..models.similar_profiles_success_meta import SimilarProfilesSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = SimilarProfilesData.from_dict(d.pop("data"))

        meta = SimilarProfilesSuccessMeta.from_dict(d.pop("meta"))

        similar_profiles_success = cls(
            data=data,
            meta=meta,
        )

        return similar_profiles_success
