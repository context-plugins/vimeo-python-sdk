from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status23(str, Enum):
    """The status code for the availability of the video version.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The video version is available.
     * ``error`` - There was a transcoding error. The video version isn't available.
     * ``in_progress`` - Transcoding is in progress. The video version isn't available yet."""

    COMPLETE = "complete"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status23OrStr: TypeAlias = Annotated[Status23 | str, open_enum_validator(Status23)]
