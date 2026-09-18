from enum import StrEnum


class CompanyPostsFilter(StrEnum):
    ALL = "ALL"
    ARTICLES = "ARTICLES"
    DOCUMENTS = "DOCUMENTS"
    IMAGES = "IMAGES"
    VIDEOS = "VIDEOS"

    def __str__(self) -> str:
        return str(self.value)
