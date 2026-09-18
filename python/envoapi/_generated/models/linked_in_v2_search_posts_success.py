from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_search_posts_success_meta import LinkedInV2SearchPostsSuccessMeta
    from ..models.search_posts_data import SearchPostsData


T = TypeVar("T", bound="LinkedInV2SearchPostsSuccess")


@_attrs_define
class LinkedInV2SearchPostsSuccess:
    """
    Attributes:
        data (SearchPostsData):
        meta (LinkedInV2SearchPostsSuccessMeta):
    """

    data: SearchPostsData
    meta: LinkedInV2SearchPostsSuccessMeta

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
        from ..models.linked_in_v2_search_posts_success_meta import LinkedInV2SearchPostsSuccessMeta  # noqa: PLC0415
        from ..models.search_posts_data import SearchPostsData  # noqa: PLC0415

        d = dict(src_dict)
        data = SearchPostsData.from_dict(d.pop("data"))

        meta = LinkedInV2SearchPostsSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_search_posts_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_search_posts_success
