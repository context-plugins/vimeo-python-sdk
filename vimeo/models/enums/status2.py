from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status2(str, Enum):
    """The status of the video.

    Option descriptions:
     * ``done`` - The video is finished processing.
     * ``failed`` - Video processing has failed.
     * ``processing`` - The video is still being processed."""

    DONE = "done"
    FAILED = "failed"
    PROCESSING = "processing"

    __str__ = str.__str__


Status2OrStr: TypeAlias = Annotated[Status2 | str, open_enum_validator(Status2)]
