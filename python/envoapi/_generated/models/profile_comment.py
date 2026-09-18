from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProfileComment")


@_attrs_define
class ProfileComment:
    """
    Attributes:
        text (str):
        created_at (datetime.datetime):
        edited (bool):
        author_name (str):
        author_headline (None | str):
        author_profile_url (str):
        reaction_count (int):
        reply_count (int):
        post_url (str):
        post_text (None | str):
        post_author_name (str):
        post_author_headline (None | str):
    """

    text: str
    created_at: datetime.datetime
    edited: bool
    author_name: str
    author_headline: None | str
    author_profile_url: str
    reaction_count: int
    reply_count: int
    post_url: str
    post_text: None | str
    post_author_name: str
    post_author_headline: None | str

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        created_at = self.created_at.isoformat()

        edited = self.edited

        author_name = self.author_name

        author_headline: None | str
        author_headline = self.author_headline

        author_profile_url = self.author_profile_url

        reaction_count = self.reaction_count

        reply_count = self.reply_count

        post_url = self.post_url

        post_text: None | str
        post_text = self.post_text

        post_author_name = self.post_author_name

        post_author_headline: None | str
        post_author_headline = self.post_author_headline

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "createdAt": created_at,
                "edited": edited,
                "authorName": author_name,
                "authorHeadline": author_headline,
                "authorProfileUrl": author_profile_url,
                "reactionCount": reaction_count,
                "replyCount": reply_count,
                "postUrl": post_url,
                "postText": post_text,
                "postAuthorName": post_author_name,
                "postAuthorHeadline": post_author_headline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")
        if not isinstance(text, str):
            raise TypeError("Expected string for text")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        edited = d.pop("edited")

        author_name = d.pop("authorName")
        if not isinstance(author_name, str):
            raise TypeError("Expected string for author_name")

        def _parse_author_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author_headline = _parse_author_headline(d.pop("authorHeadline"))

        author_profile_url = d.pop("authorProfileUrl")
        if not isinstance(author_profile_url, str):
            raise TypeError("Expected string for author_profile_url")

        reaction_count = d.pop("reactionCount")

        reply_count = d.pop("replyCount")

        post_url = d.pop("postUrl")
        if not isinstance(post_url, str):
            raise TypeError("Expected string for post_url")

        def _parse_post_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_text = _parse_post_text(d.pop("postText"))

        post_author_name = d.pop("postAuthorName")
        if not isinstance(post_author_name, str):
            raise TypeError("Expected string for post_author_name")

        def _parse_post_author_headline(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_author_headline = _parse_post_author_headline(d.pop("postAuthorHeadline"))

        profile_comment = cls(
            text=text,
            created_at=created_at,
            edited=edited,
            author_name=author_name,
            author_headline=author_headline,
            author_profile_url=author_profile_url,
            reaction_count=reaction_count,
            reply_count=reply_count,
            post_url=post_url,
            post_text=post_text,
            post_author_name=post_author_name,
            post_author_headline=post_author_headline,
        )

        return profile_comment
