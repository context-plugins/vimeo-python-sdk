from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StreamMode(str, Enum):
    """The stream mode of the event.

    Option descriptions:
     * ``live`` - The stream is live playback.
     * ``record`` - The stream is in record mode.
     * ``simulive`` - The stream is scheduled media playback."""

    LIVE = "live"
    RECORD = "record"
    SIMULIVE = "simulive"

    __str__ = str.__str__


StreamModeOrStr: TypeAlias = Annotated[StreamMode | str, open_enum_validator(StreamMode)]
