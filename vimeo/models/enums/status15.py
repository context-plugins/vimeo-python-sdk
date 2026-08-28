from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status15(str, Enum):
    """The status of the event.

    Option descriptions:
     * ``ended`` - The event has ended.
     * ``started`` - The event has started."""

    ENDED = "ended"
    STARTED = "started"

    __str__ = str.__str__


Status15OrStr: TypeAlias = Annotated[Status15 | str, open_enum_validator(Status15)]
