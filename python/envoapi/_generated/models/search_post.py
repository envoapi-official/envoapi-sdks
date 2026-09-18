from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.search_post_content_type import SearchPostContentType

if TYPE_CHECKING:
    from ..models.search_post_author import SearchPostAuthor


T = TypeVar("T", bound="SearchPost")


@_attrs_define
class SearchPost:
    """
    Attributes:
        url (str):
        text (None | str):
        author (SearchPostAuthor):
        content_type (SearchPostContentType):
        is_repost (bool):
        reaction_count (int):
        comment_count (int):
        repost_count (int):
    """

    url: str
    text: None | str
    author: SearchPostAuthor
    content_type: SearchPostContentType
    is_repost: bool
    reaction_count: int
    comment_count: int
    repost_count: int

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        text: None | str
        text = self.text

        author = self.author.to_dict()

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
                "author": author,
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
        from ..models.search_post_author import SearchPostAuthor  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        author = SearchPostAuthor.from_dict(d.pop("author"))

        content_type = SearchPostContentType(d.pop("contentType"))

        is_repost = d.pop("isRepost")

        reaction_count = d.pop("reactionCount")

        comment_count = d.pop("commentCount")

        repost_count = d.pop("repostCount")

        search_post = cls(
            url=url,
            text=text,
            author=author,
            content_type=content_type,
            is_repost=is_repost,
            reaction_count=reaction_count,
            comment_count=comment_count,
            repost_count=repost_count,
        )

        return search_post
