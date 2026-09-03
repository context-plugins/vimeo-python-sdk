from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status11(str, Enum):
    """The status of the event.

    Option descriptions:
     * ``ended`` - The user ended the event.
     * ``started`` - The user started the event."""

    ENDED = "ended"
    STARTED = "started"

    __str__ = str.__str__


Status11OrStr: TypeAlias = Annotated[Status11 | str, open_enum_validator(Status11)]
