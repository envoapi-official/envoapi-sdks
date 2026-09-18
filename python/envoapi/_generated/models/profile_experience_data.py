from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.position_item import PositionItem


T = TypeVar("T", bound="ProfileExperienceData")


@_attrs_define
class ProfileExperienceData:
    """
    Attributes:
        positions (list[PositionItem]):
    """

    positions: list[PositionItem]

    def to_dict(self) -> dict[str, Any]:
        positions = []
        for componentsschemas_position_list_item_data in self.positions:
            componentsschemas_position_list_item = componentsschemas_position_list_item_data.to_dict()
            positions.append(componentsschemas_position_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "positions": positions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position_item import PositionItem  # noqa: PLC0415

        d = dict(src_dict)
        positions = []
        _positions = d.pop("positions")
        for componentsschemas_position_list_item_data in _positions:
            componentsschemas_position_list_item = PositionItem.from_dict(componentsschemas_position_list_item_data)

            positions.append(componentsschemas_position_list_item)

        profile_experience_data = cls(
            positions=positions,
        )

        return profile_experience_data
