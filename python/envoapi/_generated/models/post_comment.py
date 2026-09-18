from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.post_comment_reply import PostCommentReply
    from ..models.post_details_author_type_0 import PostDetailsAuthorType0
    from ..models.post_details_author_type_1 import PostDetailsAuthorType1


T = TypeVar("T", bound="PostComment")


@_attrs_define
class PostComment:
    """
    Attributes:
        text (str):
        created_at (datetime.datetime | None):
        edited (bool | None):
        author (PostDetailsAuthorType0 | PostDetailsAuthorType1):
        reaction_count (int):
        reply_count (int):
        replies (list[PostCommentReply]):
    """

    text: str
    created_at: datetime.datetime | None
    edited: bool | None
    author: PostDetailsAuthorType0 | PostDetailsAuthorType1
    reaction_count: int
    reply_count: int
    replies: list[PostCommentReply]

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_details_author_type_0 import PostDetailsAuthorType0  # noqa: PLC0415

        text = self.text

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        edited: bool | None
        edited = self.edited

        author: dict[str, Any]
        if isinstance(self.author, PostDetailsAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author.to_dict()

        reaction_count = self.reaction_count

        reply_count = self.reply_count

        replies = []
        for replies_item_data in self.replies:
            replies_item = replies_item_data.to_dict()
            replies.append(replies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "createdAt": created_at,
                "edited": edited,
                "author": author,
                "reactionCount": reaction_count,
                "replyCount": reply_count,
                "replies": replies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_comment_reply import PostCommentReply  # noqa: PLC0415
        from ..models.post_details_author_type_0 import PostDetailsAuthorType0  # noqa: PLC0415
        from ..models.post_details_author_type_1 import PostDetailsAuthorType1  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")
        if not isinstance(text, str):
            raise TypeError("Expected string for text")

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("createdAt"))

        def _parse_edited(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        edited = _parse_edited(d.pop("edited"))

        def _parse_author(data: object) -> PostDetailsAuthorType0 | PostDetailsAuthorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_post_details_author_type_0 = PostDetailsAuthorType0.from_dict(data)

                return componentsschemas_post_details_author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_post_details_author_type_1 = PostDetailsAuthorType1.from_dict(data)

            return componentsschemas_post_details_author_type_1

        author = _parse_author(d.pop("author"))

        reaction_count = d.pop("reactionCount")

        reply_count = d.pop("replyCount")

        replies = []
        _replies = d.pop("replies")
        for replies_item_data in _replies:
            replies_item = PostCommentReply.from_dict(replies_item_data)

            replies.append(replies_item)

        post_comment = cls(
            text=text,
            created_at=created_at,
            edited=edited,
            author=author,
            reaction_count=reaction_count,
            reply_count=reply_count,
            replies=replies,
        )

        return post_comment
