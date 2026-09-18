from enum import StrEnum


class LinkedInV2ActivityQueryKind(StrEnum):
    COMMENTS = "comments"
    POSTS = "posts"
    REACTIONS = "reactions"

    def __str__(self) -> str:
        return str(self.value)
