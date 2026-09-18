from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_details_data import PostDetailsData
    from ..models.post_details_success_meta import PostDetailsSuccessMeta


T = TypeVar("T", bound="PostDetailsSuccess")


@_attrs_define
class PostDetailsSuccess:
    """
    Attributes:
        data (PostDetailsData):
        meta (PostDetailsSuccessMeta):
    """

    data: PostDetailsData
    meta: PostDetailsSuccessMeta

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
        from ..models.post_details_data import PostDetailsData  # noqa: PLC0415
        from ..models.post_details_success_meta import PostDetailsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = PostDetailsData.from_dict(d.pop("data"))

        meta = PostDetailsSuccessMeta.from_dict(d.pop("meta"))

        post_details_success = cls(
            data=data,
            meta=meta,
        )

        return post_details_success
