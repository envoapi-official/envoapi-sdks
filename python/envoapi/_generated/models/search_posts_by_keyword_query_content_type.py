from enum import StrEnum


class SearchPostsByKeywordQueryContentType(StrEnum):
    COLLABORATIVEARTICLES = "collaborativeArticles"
    DOCUMENTS = "documents"
    JOBS = "jobs"
    LIVEVIDEOS = "liveVideos"
    PHOTOS = "photos"
    VIDEOS = "videos"

    def __str__(self) -> str:
        return str(self.value)
