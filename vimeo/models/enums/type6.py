from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type6(str, Enum):
    """The type of video file.

    Option descriptions:
     * ``source`` - The video file is a source file.
     * ``video/mp4`` - The video file is in MP4 format.
     * ``video/webm`` - The video file is in WebM format.
     * ``vp6/x-video`` - The video file is in VP6 format."""

    SOURCE = "source"
    VIDEO_MP4 = "video/mp4"
    VIDEO_WEBM = "video/webm"
    VP6_X_VIDEO = "vp6/x-video"

    __str__ = str.__str__


Type6OrStr: TypeAlias = Annotated[Type6 | str, open_enum_validator(Type6)]
