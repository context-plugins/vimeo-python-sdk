from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status13(str, Enum):
    """The status of the event.

    Option descriptions:
     * ``ended`` - The user ended the event.
     * ``started`` - The user started the event."""

    ENDED = "ended"
    STARTED = "started"

    __str__ = str.__str__


Status13OrStr: TypeAlias = Annotated[Status13 | str, open_enum_validator(Status13)]
