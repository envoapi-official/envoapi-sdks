from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.company_person import CompanyPerson


T = TypeVar("T", bound="CompanyPeopleData")


@_attrs_define
class CompanyPeopleData:
    """
    Attributes:
        people (list[CompanyPerson]):
    """

    people: list[CompanyPerson]

    def to_dict(self) -> dict[str, Any]:
        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "people": people,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_person import CompanyPerson  # noqa: PLC0415

        d = dict(src_dict)
        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = CompanyPerson.from_dict(people_item_data)

            people.append(people_item)

        company_people_data = cls(
            people=people,
        )

        return company_people_data
