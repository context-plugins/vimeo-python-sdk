from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status10(str, Enum):
    """The status of the pre-live video's RTMP link.

    Option descriptions:
     * ``pending`` - Vimeo is working on setting up the connection.
     * ``ready`` - Resources have been provisioned for the event.
     * ``streaming`` - Live video is currently streaming to the RTMP link.
     * ``unavailable`` - The connection is ready, but streaming to the RTMP link has not yet begun."""

    PENDING = "pending"
    READY = "ready"
    STREAMING = "streaming"
    UNAVAILABLE = "unavailable"

    __str__ = str.__str__


Status10OrStr: TypeAlias = Annotated[Status10 | str, open_enum_validator(Status10)]
