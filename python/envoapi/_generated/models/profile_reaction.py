from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_reaction_post_content_type import ProfileReactionPostContentType
from ..models.profile_reaction_reaction_type import ProfileReactionReactionType

T = TypeVar("T", bound="ProfileReaction")


@_attrs_define
class ProfileReaction:
    """
    Attributes:
        reaction_type (ProfileReactionReactionType):
        reactor_name (str):
        reactor_profile_url (str):
        post_url (str):
        post_text (None | str):
        post_author_name (str):
        post_author_headline (None | str):
        post_author_profile_url (None | str):
        post_content_type (ProfileReactionPostContentType):
        post_is_repost (bool):
        post_reaction_count (int):
        post_comment_count (int):
        post_repost_count (int):
    """

    reaction_type: ProfileReactionReactionType
    reactor_name: str
    reactor_profile_url: str
    post_url: str
    post_text: None | str
    post_author_name: str
    post_author_headline: None | str
    post_author_profile_url: None | str
    post_content_type: ProfileReactionPostContentType
    post_is_repost: bool
    post_reaction_count: int
    post_comment_count: int
    post_repost_count: int

    def to_dict(self) -> dict[str, Any]:
        reaction_type = self.reaction_type.value

        reactor_name = self.reactor_name

        reactor_profile_url = self.reactor_profile_url

        post_url = self.post_url

        post_text: None | str
        post_text = self.post_text

        post_author_name = self.post_author_name

        post_author_headline: None | str
        post_author_headline = self.post_author_headline

        post_author_profile_url: None | str
        post_author_profile_url = self.post_author_profile_url

        post_content_type = self.post_content_type.value

        post_is_repost = self.post_is_repost

        post_reaction_count = self.post_reaction_count

        post_comment_count = self.post_comment_count

        post_repost_count = self.post_repost_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reactionType": reaction_type,
                "reactorName": reactor_name,
                "reactorProfileUrl": reactor_profile_url,
                "postUrl": post_url,
                "postText": post_text,
                "postAuthorName": post_author_name,
                "postAuthorHeadline": post_author_headline,
                "postAuthorProfileUrl": post_author_profile_url,
                "postContentType": post_content_type,
                "postIsRepost": post_is_repost,
                "postReactionCount": post_reaction_count,
                "postCommentCount": post_comment_count,
                "postRepostCount": post_repost_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reaction_type = ProfileReactionReactionType(d.pop("reactionType"))

        reactor_name = d.pop("reactorName")
        if not isinstance(reactor_name, str):
            raise TypeError("Expected string for reactor_name")

        reactor_profile_url = d.pop("reactorProfileUrl")
        if not isinstance(reactor_profile_url, str):
            raise TypeError("Expected string for reactor_profile_url")

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

        def _parse_post_author_profile_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_author_profile_url = _parse_post_author_profile_url(d.pop("postAuthorProfileUrl"))

        post_content_type = ProfileReactionPostContentType(d.pop("postContentType"))

        post_is_repost = d.pop("postIsRepost")

        post_reaction_count = d.pop("postReactionCount")

        post_comment_count = d.pop("postCommentCount")

        post_repost_count = d.pop("postRepostCount")

        profile_reaction = cls(
            reaction_type=reaction_type,
            reactor_name=reactor_name,
            reactor_profile_url=reactor_profile_url,
            post_url=post_url,
            post_text=post_text,
            post_author_name=post_author_name,
            post_author_headline=post_author_headline,
            post_author_profile_url=post_author_profile_url,
            post_content_type=post_content_type,
            post_is_repost=post_is_repost,
            post_reaction_count=post_reaction_count,
            post_comment_count=post_comment_count,
            post_repost_count=post_repost_count,
        )

        return profile_reaction
