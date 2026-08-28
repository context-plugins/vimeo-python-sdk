from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type10(str, Enum):
    """The activity type.

    Option descriptions:
     * ``appearance`` - The activity is an appearance action.
     * ``category`` - The activity is a category action.
     * ``channel`` - The activity is a channel action.
     * ``facebook_feed`` - The activity is a Facebook feed action.
     * ``group`` - The activity is a group action.
     * ``like`` - The activity is a like action.
     * ``ondemand`` - The activity is a Vimeo On Demand action.
     * ``share`` - The activity is a share action.
     * ``tag`` - The activity is a tag action.
     * ``twitter_timeline`` - The activity is a Twitter timeline action.
     * ``upload`` - The activity is an upload action."""

    APPEARANCE = "appearance"
    CATEGORY = "category"
    CHANNEL = "channel"
    FACEBOOK_FEED = "facebook_feed"
    GROUP = "group"
    LIKE = "like"
    ONDEMAND = "ondemand"
    SHARE = "share"
    TAG = "tag"
    TWITTER_TIMELINE = "twitter_timeline"
    UPLOAD = "upload"

    __str__ = str.__str__


Type10OrStr: TypeAlias = Annotated[Type10 | str, open_enum_validator(Type10)]
