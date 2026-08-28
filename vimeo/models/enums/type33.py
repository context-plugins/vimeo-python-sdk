from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type33(str, Enum):
    APPEARS = "appears"
    CATEGORY_FEATURED = "category_featured"
    CHANNEL = "channel"
    FACEBOOK_FEED = "facebook_feed"
    FOLLOWING = "following"
    GROUP = "group"
    LIKES = "likes"
    ONDEMAND_PUBLISH = "ondemand_publish"
    SHARE = "share"
    TAGGED_WITH = "tagged_with"
    TWITTER_TIMELINE = "twitter_timeline"
    UPLOADS = "uploads"

    __str__ = str.__str__


Type33OrStr: TypeAlias = Annotated[Type33 | str, open_enum_validator(Type33)]
