from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.post_reaction_reaction_type import PostReactionReactionType

if TYPE_CHECKING:
    from ..models.post_reactor_type_0 import PostReactorType0
    from ..models.post_reactor_type_1 import PostReactorType1


T = TypeVar("T", bound="PostReaction")


@_attrs_define
class PostReaction:
    """
    Attributes:
        reaction_type (PostReactionReactionType):
        reactor (PostReactorType0 | PostReactorType1):
    """

    reaction_type: PostReactionReactionType
    reactor: PostReactorType0 | PostReactorType1

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_reactor_type_0 import PostReactorType0  # noqa: PLC0415

        reaction_type = self.reaction_type.value

        reactor: dict[str, Any]
        if isinstance(self.reactor, PostReactorType0):
            reactor = self.reactor.to_dict()
        else:
            reactor = self.reactor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reactionType": reaction_type,
                "reactor": reactor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_reactor_type_0 import PostReactorType0  # noqa: PLC0415
        from ..models.post_reactor_type_1 import PostReactorType1  # noqa: PLC0415

        d = dict(src_dict)
        reaction_type = PostReactionReactionType(d.pop("reactionType"))

        def _parse_reactor(data: object) -> PostReactorType0 | PostReactorType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_post_reactor_type_0 = PostReactorType0.from_dict(data)

                return componentsschemas_post_reactor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_post_reactor_type_1 = PostReactorType1.from_dict(data)

            return componentsschemas_post_reactor_type_1

        reactor = _parse_reactor(d.pop("reactor"))

        post_reaction = cls(
            reaction_type=reaction_type,
            reactor=reactor,
        )

        return post_reaction
