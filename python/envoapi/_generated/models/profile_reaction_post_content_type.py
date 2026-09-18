from enum import StrEnum


class ProfileReactionPostContentType(StrEnum):
    ARTICLE = "article"
    DOCUMENT = "document"
    IMAGE = "image"
    OTHER = "other"
    TEXT = "text"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
