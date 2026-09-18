from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_posts_data import CompanyPostsData
    from ..models.linked_in_v2_company_posts_success_meta import LinkedInV2CompanyPostsSuccessMeta


T = TypeVar("T", bound="LinkedInV2CompanyPostsSuccess")


@_attrs_define
class LinkedInV2CompanyPostsSuccess:
    """
    Attributes:
        data (CompanyPostsData):
        meta (LinkedInV2CompanyPostsSuccessMeta):
    """

    data: CompanyPostsData
    meta: LinkedInV2CompanyPostsSuccessMeta

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
        from ..models.company_posts_data import CompanyPostsData  # noqa: PLC0415
        from ..models.linked_in_v2_company_posts_success_meta import LinkedInV2CompanyPostsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyPostsData.from_dict(d.pop("data"))

        meta = LinkedInV2CompanyPostsSuccessMeta.from_dict(d.pop("meta"))

        linked_in_v2_company_posts_success = cls(
            data=data,
            meta=meta,
        )

        return linked_in_v2_company_posts_success
