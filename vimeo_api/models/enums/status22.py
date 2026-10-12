from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status22(str, Enum):
    """The status of the video's edit session. This data requires a bearer token with the ``private`` scope.

    Option descriptions:
     * ``done`` - The video is finished processing.
     * ``failed`` - Video processing has failed.
     * ``processing`` - The video is still being processed."""

    DONE = "done"
    FAILED = "failed"
    PROCESSING = "processing"

    __str__ = str.__str__


Status22OrStr: TypeAlias = Annotated[Status22 | str, open_enum_validator(Status22)]
