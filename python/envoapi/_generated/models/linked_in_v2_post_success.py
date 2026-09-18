from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.linked_in_v2_post_success_meta import LinkedInV2PostSuccessMeta
    from ..models.post_details_data import PostDetailsData


T = TypeVar("T", bound="LinkedInV2PostSuccess")


@_attrs_define
class LinkedInV2PostSuccess:
    """
    Attributes:
        data (PostDetailsData):
        meta (LinkedInV2PostSuccessMeta):
    """

    data: PostDetailsData
    meta: LinkedInV2PostSuccessMeta

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
        from ..models.linked_in_v2_post_success_meta import LinkedInV2PostSuccessMeta  # noqa: PLC0415
        from ..models.post_details_data import PostDetailsData  # noqa: PLC0415

        d = dict(src_dict)
        data = PostDetailsData.from_dict(d.pop("data"))

        meta = LinkedInV2PostSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_post_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_post_success
