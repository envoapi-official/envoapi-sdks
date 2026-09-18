from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SchoolKeywordSearchSchool")


@_attrs_define
class SchoolKeywordSearchSchool:
    """
    Attributes:
        id (str):
        name (str):
        slug (str):
        linkedin_url (str):
        location (None | str):
        student_and_alumni_count (int | None):
        logo_url (None | str):
    """

    id: str
    name: str
    slug: str
    linkedin_url: str
    location: None | str
    student_and_alumni_count: int | None
    logo_url: None | str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        linkedin_url = self.linkedin_url

        location: None | str
        location = self.location

        student_and_alumni_count: int | None
        student_and_alumni_count = self.student_and_alumni_count

        logo_url: None | str
        logo_url = self.logo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "linkedinUrl": linkedin_url,
                "location": location,
                "studentAndAlumniCount": student_and_alumni_count,
                "logoUrl": logo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")
        if not isinstance(id, str):
            raise TypeError("Expected string for id")

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        slug = d.pop("slug")
        if not isinstance(slug, str):
            raise TypeError("Expected string for slug")

        linkedin_url = d.pop("linkedinUrl")
        if not isinstance(linkedin_url, str):
            raise TypeError("Expected string for linkedin_url")

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_student_and_alumni_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        student_and_alumni_count = _parse_student_and_alumni_count(d.pop("studentAndAlumniCount"))

        def _parse_logo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        logo_url = _parse_logo_url(d.pop("logoUrl"))

        school_keyword_search_school = cls(
            id=id,
            name=name,
            slug=slug,
            linkedin_url=linkedin_url,
            location=location,
            student_and_alumni_count=student_and_alumni_count,
            logo_url=logo_url,
        )

        return school_keyword_search_school
