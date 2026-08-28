from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamingType(str, Enum):
    """The streaming type of the video.

    Option descriptions:
     * ``live`` - The video is streamed in real time.
     * ``non-live`` - The video isn't streamed in real time."""

    LIVE = "live"
    NON_LIVE = "non-live"

    __str__ = str.__str__


StreamingTypeOrStr: TypeAlias = Annotated[StreamingType | str, open_enum_validator(StreamingType)]
