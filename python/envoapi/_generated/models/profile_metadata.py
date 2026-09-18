from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.profile_sections import ProfileSections


T = TypeVar("T", bound="ProfileMetadata")


@_attrs_define
class ProfileMetadata:
    """
    Attributes:
        request_id (str):
        fetched_at (datetime.datetime):
        partial (bool):
        sections (ProfileSections):
    """

    request_id: str
    fetched_at: datetime.datetime
    partial: bool
    sections: ProfileSections

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        fetched_at = self.fetched_at.isoformat()

        partial = self.partial

        sections = self.sections.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requestId": request_id,
                "fetchedAt": fetched_at,
                "partial": partial,
                "sections": sections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_sections import ProfileSections  # noqa: PLC0415

        d = dict(src_dict)
        request_id = d.pop("requestId")
        if not isinstance(request_id, str):
            raise TypeError("Expected string for request_id")

        fetched_at = datetime.datetime.fromisoformat(d.pop("fetchedAt"))

        partial = d.pop("partial")

        sections = ProfileSections.from_dict(d.pop("sections"))

        profile_metadata = cls(
            request_id=request_id,
            fetched_at=fetched_at,
            partial=partial,
            sections=sections,
        )

        return profile_metadata
