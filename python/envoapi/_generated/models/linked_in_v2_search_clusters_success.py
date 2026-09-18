from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.keyword_search_data import KeywordSearchData
    from ..models.linked_in_v2_search_clusters_success_meta import LinkedInV2SearchClustersSuccessMeta


T = TypeVar("T", bound="LinkedInV2SearchClustersSuccess")


@_attrs_define
class LinkedInV2SearchClustersSuccess:
    """
    Attributes:
        data (KeywordSearchData):
        meta (LinkedInV2SearchClustersSuccessMeta):
    """

    data: KeywordSearchData
    meta: LinkedInV2SearchClustersSuccessMeta

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
        from ..models.keyword_search_data import KeywordSearchData  # noqa: PLC0415
        from ..models.linked_in_v2_search_clusters_success_meta import (
            LinkedInV2SearchClustersSuccessMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        data = KeywordSearchData.from_dict(d.pop("data"))

        meta = LinkedInV2SearchClustersSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_search_clusters_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_search_clusters_success
