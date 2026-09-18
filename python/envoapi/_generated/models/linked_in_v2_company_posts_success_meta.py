from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_posts_cursor_paging import CompanyPostsCursorPaging
    from ..models.company_posts_paging_type_1 import CompanyPostsPagingType1


T = TypeVar("T", bound="LinkedInV2CompanyPostsSuccessMeta")


@_attrs_define
class LinkedInV2CompanyPostsSuccessMeta:
    """
    Attributes:
        paging (CompanyPostsCursorPaging | CompanyPostsPagingType1):
        credit_cost (int):
    """

    paging: CompanyPostsCursorPaging | CompanyPostsPagingType1
    credit_cost: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_posts_cursor_paging import CompanyPostsCursorPaging  # noqa: PLC0415

        paging: dict[str, Any]
        if isinstance(self.paging, CompanyPostsCursorPaging):
            paging = self.paging.to_dict()
        else:
            paging = self.paging.to_dict()

        credit_cost = self.credit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "paging": paging,
                "creditCost": credit_cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_posts_cursor_paging import CompanyPostsCursorPaging  # noqa: PLC0415
        from ..models.company_posts_paging_type_1 import CompanyPostsPagingType1  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_paging(data: object) -> CompanyPostsCursorPaging | CompanyPostsPagingType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_posts_paging_type_0 = CompanyPostsCursorPaging.from_dict(data)

                return componentsschemas_company_posts_paging_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_company_posts_paging_type_1 = CompanyPostsPagingType1.from_dict(data)

            return componentsschemas_company_posts_paging_type_1

        paging = _parse_paging(d.pop("paging"))

        credit_cost = d.pop("creditCost")

        linked_in_v2_company_posts_success_meta = cls(
            paging=paging,
            credit_cost=credit_cost,
        )

        return linked_in_v2_company_posts_success_meta
