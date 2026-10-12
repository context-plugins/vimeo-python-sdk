from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status9(str, Enum):
    """The transcode status of the audio track.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The audio track is available.
     * ``error`` - There was a transcoding error. The audio track isn't available.
     * ``in_progress`` - Transcoding is in progress. The audio track isn't available yet."""

    COMPLETE = "complete"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status9OrStr: TypeAlias = Annotated[Status9 | str, open_enum_validator(Status9)]
