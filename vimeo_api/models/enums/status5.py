from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status5(str, Enum):
    """The video's availability status.

    Option descriptions:
     * ``complete`` - Transcoding is complete. The video is available.
     * ``error`` - There was a transcoding error. The video isn't available.
     * ``in_progress`` - Transcoding is currently underway. The video isn't available yet."""

    COMPLETE = "complete"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status5OrStr: TypeAlias = Annotated[Status5 | str, open_enum_validator(Status5)]
