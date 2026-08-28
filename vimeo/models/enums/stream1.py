from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Stream1(str, Enum):
    """The user's streaming access to the On Demand video.

    Option descriptions:
     * ``available`` - The video is available for streaming.
     * ``purchased`` - The user has purchased the video.
     * ``restricted`` - The user isn't permitted to stream the video.
     * ``unavailable`` - The video isn't available for streaming."""

    AVAILABLE = "available"
    PURCHASED = "purchased"
    RESTRICTED = "restricted"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Stream1OrStr: TypeAlias = Annotated[Stream1 | str, open_enum_validator(Stream1)]
