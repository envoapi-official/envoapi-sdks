from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_post_content_type import ProfilePostContentType

T = TypeVar("T", bound="ProfilePost")


@_attrs_define
class ProfilePost:
    """
    Attributes:
        url (str):
        text (None | str):
        author_name (str):
        author_headline (None | str):
        author_profile_url (None | str):
        content_type (ProfilePostContentType):
        is_repost (bool):
        reaction_count (int):
        comment_count (int):
        repost_count (int):
    """

    url: str
    text: None | str
    author_name: str
    author_headline: None | str
    author_profile_url: None | str
    content_type: ProfilePostContentType
    is_repost: bool
    reaction_count: int
    comment_count: int
    repost_count: int

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        text: None | str
        text = self.text

        author_name = self.author_name

        author_headline: None | str
        author_headline = self.author_headline

        author_profile_url: None | str
        author_profile_url = self.author_profile_url

        content_type = self.content_type.value

        is_repost = self.is_repost

        reaction_count = self.reaction_count

        comment_count = self.comment_count

        repost_count = self.repost_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "text": text,
                "authorName": author_name,
                "authorHeadline": author_headline,
                "authorProfileUrl": author_profile_url,
                "contentType": content_type,
                "isRepost": is_repost,
                "reactionCount": reaction_count,
                "commentCount": comment_count,
                "repostCount": repost_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        author_name = d.pop("authorName")
        if not isinstance(author_name, str):
            raise TypeError("Expected string for author_name")

        def _parse_author_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author_headline = _parse_author_headline(d.pop("authorHeadline"))

        def _parse_author_profile_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author_profile_url = _parse_author_profile_url(d.pop("authorProfileUrl"))

        content_type = ProfilePostContentType(d.pop("contentType"))

        is_repost = d.pop("isRepost")

        reaction_count = d.pop("reactionCount")

        comment_count = d.pop("commentCount")

        repost_count = d.pop("repostCount")

        profile_post = cls(
            url=url,
            text=text,
            author_name=author_name,
            author_headline=author_headline,
            author_profile_url=author_profile_url,
            content_type=content_type,
            is_repost=is_repost,
            reaction_count=reaction_count,
            comment_count=comment_count,
            repost_count=repost_count,
        )

        return profile_post
