from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.post_details_data_content_type import PostDetailsDataContentType

if TYPE_CHECKING:
    from ..models.post_details_author_type_0 import PostDetailsAuthorType0
    from ..models.post_details_author_type_1 import PostDetailsAuthorType1
    from ..models.post_reaction_count import PostReactionCount


T = TypeVar("T", bound="PostDetailsData")


@_attrs_define
class PostDetailsData:
    """
    Attributes:
        url (str):
        text (None | str):
        author (PostDetailsAuthorType0 | PostDetailsAuthorType1):
        content_type (PostDetailsDataContentType):
        is_repost (bool):
        reaction_count (int):
        comment_count (int):
        repost_count (int):
        reactions (list[PostReactionCount]):
    """

    url: str
    text: None | str
    author: PostDetailsAuthorType0 | PostDetailsAuthorType1
    content_type: PostDetailsDataContentType
    is_repost: bool
    reaction_count: int
    comment_count: int
    repost_count: int
    reactions: list[PostReactionCount]

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_details_author_type_0 import PostDetailsAuthorType0  # noqa: PLC0415

        url = self.url

        text: None | str
        text = self.text

        author: dict[str, Any]
        if isinstance(self.author, PostDetailsAuthorType0):
            author = self.author.to_dict()
        else:
            author = self.author.to_dict()

        content_type = self.content_type.value

        is_repost = self.is_repost

        reaction_count = self.reaction_count

        comment_count = self.comment_count

        repost_count = self.repost_count

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()
            reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "text": text,
                "author": author,
                "contentType": content_type,
                "isRepost": is_repost,
                "reactionCount": reaction_count,
                "commentCount": comment_count,
                "repostCount": repost_count,
                "reactions": reactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_details_author_type_0 import PostDetailsAuthorType0  # noqa: PLC0415
        from ..models.post_details_author_type_1 import PostDetailsAuthorType1  # noqa: PLC0415
        from ..models.post_reaction_count import PostReactionCount  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

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

        content_type = PostDetailsDataContentType(d.pop("contentType"))

        is_repost = d.pop("isRepost")

        reaction_count = d.pop("reactionCount")

        comment_count = d.pop("commentCount")

        repost_count = d.pop("repostCount")

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = PostReactionCount.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        post_details_data = cls(
            url=url,
            text=text,
            author=author,
            content_type=content_type,
            is_repost=is_repost,
            reaction_count=reaction_count,
            comment_count=comment_count,
            repost_count=repost_count,
            reactions=reactions,
        )

        return post_details_data
