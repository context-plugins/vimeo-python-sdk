from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutroVideosCollectionType(str, Enum):
    """The source of the video collection that appears in the area for more videos.

    Option descriptions:
     * ``album`` - The video collection source is a user showcase.
     * ``all_videos`` - The video collection source is all user videos.
     * ``channel`` - The video collection source is a user channel.
     * ``group`` - The video collection source is a user group.
     * ``likes`` - The video collection source is user likes.
     * ``uploaded_videos`` - The video collection source is user uploads."""

    ALBUM = "album"
    ALL_VIDEOS = "all_videos"
    CHANNEL = "channel"
    GROUP = "group"
    LIKES = "likes"
    UPLOADED_VIDEOS = "uploaded_videos"

    __str__ = str.__str__


OutroVideosCollectionTypeOrStr: TypeAlias = Annotated[
    OutroVideosCollectionType | str, open_enum_validator(OutroVideosCollectionType)
]
