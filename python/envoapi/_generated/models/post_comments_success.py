from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_comments_data import PostCommentsData
    from ..models.post_comments_success_meta import PostCommentsSuccessMeta


T = TypeVar("T", bound="PostCommentsSuccess")


@_attrs_define
class PostCommentsSuccess:
    """
    Attributes:
        data (PostCommentsData):
        meta (PostCommentsSuccessMeta):
    """

    data: PostCommentsData
    meta: PostCommentsSuccessMeta

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
        from ..models.post_comments_data import PostCommentsData  # noqa: PLC0415
        from ..models.post_comments_success_meta import PostCommentsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = PostCommentsData.from_dict(d.pop("data"))

        meta = PostCommentsSuccessMeta.from_dict(d.pop("meta"))

        post_comments_success = cls(
            data=data,
            meta=meta,
        )

        return post_comments_success
