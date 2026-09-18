from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_reactions_data import PostReactionsData
    from ..models.post_reactions_success_meta import PostReactionsSuccessMeta


T = TypeVar("T", bound="PostReactionsSuccess")


@_attrs_define
class PostReactionsSuccess:
    """
    Attributes:
        data (PostReactionsData):
        meta (PostReactionsSuccessMeta):
    """

    data: PostReactionsData
    meta: PostReactionsSuccessMeta

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
        from ..models.post_reactions_data import PostReactionsData  # noqa: PLC0415
        from ..models.post_reactions_success_meta import PostReactionsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = PostReactionsData.from_dict(d.pop("data"))

        meta = PostReactionsSuccessMeta.from_dict(d.pop("meta"))

        post_reactions_success = cls(
            data=data,
            meta=meta,
        )

        return post_reactions_success
