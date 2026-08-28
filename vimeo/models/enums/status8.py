from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status8(str, Enum):
    """The status code for the availability of the uploaded video.

    Option descriptions:
     * ``canceled`` - The upload was canceled.
     * ``complete`` - The upload is complete.
     * ``error`` - The upload ended with an error.
     * ``in_progress`` - The upload is underway."""

    CANCELED = "canceled"
    COMPLETE = "complete"
    ERROR = "error"
    IN_PROGRESS = "in_progress"

    __str__ = str.__str__


Status8OrStr: TypeAlias = Annotated[Status8 | str, open_enum_validator(Status8)]
