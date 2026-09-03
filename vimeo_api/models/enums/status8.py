from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status8(str, Enum):
    """The transcode status of the audio track.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The audio track is available.
     * ``error`` - There was a transcoding error. The audio track isn't available.
     * ``in_progress`` - Transcoding is in progress. The audio track isn't available yet."""

    COMPLETE = "complete"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status8OrStr: TypeAlias = Annotated[Status8 | str, open_enum_validator(Status8)]
