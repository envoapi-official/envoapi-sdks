from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.company_post_content_type import CompanyPostContentType

if TYPE_CHECKING:
    from ..models.company_post_author_type_0 import CompanyPostAuthorType0
    from ..models.company_post_author_type_1 import CompanyPostAuthorType1


T = TypeVar("T", bound="CompanyPost")


@_attrs_define
class CompanyPost:
    """
    Attributes:
        url (str):
        text (None | str):
        author (CompanyPostAuthorType0 | CompanyPostAuthorType1):
        content_type (CompanyPostContentType):
        is_repost (bool):
        reaction_count (int):
        comment_count (int):
        repost_count (int):
    """

    url: str
    text: None | str
    author: CompanyPostAuthorType0 | CompanyPostAuthorType1
    content_type: CompanyPostContentType
    is_repost: bool
    reaction_count: int
    comment_count: int
    repost_count: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_post_author_type_0 import CompanyPostAuthorType0  # noqa: PLC0415

        url = self.url

        text: None | str
        text = self.text

        author: dict[str, Any]
        if isinstance(self.author, CompanyPostAuthorType0):
            author = self.author.to_dict()
        else:
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
        from ..models.company_post_author_type_0 import CompanyPostAuthorType0  # noqa: PLC0415
        from ..models.company_post_author_type_1 import CompanyPostAuthorType1  # noqa: PLC0415

        d = dict(src_dict)
        url = d.pop("url")
        if not isinstance(url, str):
            raise TypeError("Expected string for url")

        def _parse_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        text = _parse_text(d.pop("text"))

        def _parse_author(data: object) -> CompanyPostAuthorType0 | CompanyPostAuthorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_post_author_type_0 = CompanyPostAuthorType0.from_dict(data)

                return componentsschemas_company_post_author_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_company_post_author_type_1 = CompanyPostAuthorType1.from_dict(data)

            return componentsschemas_company_post_author_type_1

        author = _parse_author(d.pop("author"))

        content_type = CompanyPostContentType(d.pop("contentType"))

        is_repost = d.pop("isRepost")

        reaction_count = d.pop("reactionCount")

        comment_count = d.pop("commentCount")

        repost_count = d.pop("repostCount")

        company_post = cls(
            url=url,
            text=text,
            author=author,
            content_type=content_type,
            is_repost=is_repost,
            reaction_count=reaction_count,
            comment_count=comment_count,
            repost_count=repost_count,
        )

        return company_post
