from enum import StrEnum


class SocialHandlePlatform(StrEnum):
    TWITTER = "twitter"
    WECHAT = "wechat"

    def __str__(self) -> str:
        return str(self.value)
