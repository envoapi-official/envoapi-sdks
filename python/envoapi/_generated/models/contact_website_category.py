from enum import StrEnum


class ContactWebsiteCategory(StrEnum):
    BLOG = "blog"
    COMPANY = "company"
    OTHER = "other"
    PERSONAL = "personal"
    PORTFOLIO = "portfolio"
    RSS = "rss"

    def __str__(self) -> str:
        return str(self.value)
