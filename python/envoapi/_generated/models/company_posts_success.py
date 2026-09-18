from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_posts_data import CompanyPostsData
    from ..models.company_posts_success_meta import CompanyPostsSuccessMeta


T = TypeVar("T", bound="CompanyPostsSuccess")


@_attrs_define
class CompanyPostsSuccess:
    """
    Attributes:
        data (CompanyPostsData):
        meta (CompanyPostsSuccessMeta):
    """

    data: CompanyPostsData
    meta: CompanyPostsSuccessMeta

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
        from ..models.company_posts_success_meta import CompanyPostsSuccessMeta  # noqa: PLC0415

        d = dict(src_dict)
        data = CompanyPostsData.from_dict(d.pop("data"))

        meta = CompanyPostsSuccessMeta.from_dict(d.pop("meta"))

        company_posts_success = cls(
            data=data,
            meta=meta,
        )

        return company_posts_success
