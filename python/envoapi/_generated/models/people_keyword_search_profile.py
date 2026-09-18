from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.people_keyword_search_profile_education_item import PeopleKeywordSearchProfileEducationItem
    from ..models.people_keyword_search_profile_positions_item import PeopleKeywordSearchProfilePositionsItem


T = TypeVar("T", bound="PeopleKeywordSearchProfile")


@_attrs_define
class PeopleKeywordSearchProfile:
    """
    Attributes:
        public_id (None | str):
        name (str):
        first_name (None | str):
        last_name (None | str):
        headline (None | str):
        summary (None | str):
        location (None | str):
        country_iso_code (None | str):
        industry (None | str):
        linkedin_url (str):
        profile_picture_url (None | str):
        positions (list[PeopleKeywordSearchProfilePositionsItem]):
        education (list[PeopleKeywordSearchProfileEducationItem]):
        skills (list[str]):
        premium (bool | None):
        creator (bool | None):
        influencer (bool | None):
    """

    public_id: None | str
    name: str
    first_name: None | str
    last_name: None | str
    headline: None | str
    summary: None | str
    location: None | str
    country_iso_code: None | str
    industry: None | str
    linkedin_url: str
    profile_picture_url: None | str
    positions: list[PeopleKeywordSearchProfilePositionsItem]
    education: list[PeopleKeywordSearchProfileEducationItem]
    skills: list[str]
    premium: bool | None
    creator: bool | None
    influencer: bool | None

    def to_dict(self) -> dict[str, Any]:
        public_id: None | str
        public_id = self.public_id

        name = self.name

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        headline: None | str
        headline = self.headline

        summary: None | str
        summary = self.summary

        location: None | str
        location = self.location

        country_iso_code: None | str
        country_iso_code = self.country_iso_code

        industry: None | str
        industry = self.industry

        linkedin_url = self.linkedin_url

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        education = []
        for education_item_data in self.education:
            education_item = education_item_data.to_dict()
            education.append(education_item)

        skills = self.skills

        premium: bool | None
        premium = self.premium

        creator: bool | None
        creator = self.creator

        influencer: bool | None
        influencer = self.influencer

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "publicId": public_id,
                "name": name,
                "firstName": first_name,
                "lastName": last_name,
                "headline": headline,
                "summary": summary,
                "location": location,
                "countryISOCode": country_iso_code,
                "industry": industry,
                "linkedinUrl": linkedin_url,
                "profilePictureUrl": profile_picture_url,
                "positions": positions,
                "education": education,
                "skills": skills,
                "premium": premium,
                "creator": creator,
                "influencer": influencer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.people_keyword_search_profile_education_item import (
            PeopleKeywordSearchProfileEducationItem,  # noqa: PLC0415
        )
        from ..models.people_keyword_search_profile_positions_item import (
            PeopleKeywordSearchProfilePositionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_public_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_id = _parse_public_id(d.pop("publicId"))

        name = d.pop("name")
        if not isinstance(name, str):
            raise TypeError("Expected string for name")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        def _parse_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        headline = _parse_headline(d.pop("headline"))

        def _parse_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_location(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location = _parse_location(d.pop("location"))

        def _parse_country_iso_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_iso_code = _parse_country_iso_code(d.pop("countryISOCode"))

        def _parse_industry(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        industry = _parse_industry(d.pop("industry"))

        linkedin_url = d.pop("linkedinUrl")
        if not isinstance(linkedin_url, str):
            raise TypeError("Expected string for linkedin_url")

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profilePictureUrl"))

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = PeopleKeywordSearchProfilePositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        education = []
        _education = d.pop("education")
        for education_item_data in _education:
            education_item = PeopleKeywordSearchProfileEducationItem.from_dict(education_item_data)

            education.append(education_item)

        skills = cast(list[str], d.pop("skills"))

        def _parse_premium(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        premium = _parse_premium(d.pop("premium"))

        def _parse_creator(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        creator = _parse_creator(d.pop("creator"))

        def _parse_influencer(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        influencer = _parse_influencer(d.pop("influencer"))

        people_keyword_search_profile = cls(
            public_id=public_id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            headline=headline,
            summary=summary,
            location=location,
            country_iso_code=country_iso_code,
            industry=industry,
            linkedin_url=linkedin_url,
            profile_picture_url=profile_picture_url,
            positions=positions,
            education=education,
            skills=skills,
            premium=premium,
            creator=creator,
            influencer=influencer,
        )

        return people_keyword_search_profile
