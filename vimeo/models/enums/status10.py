from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status10(str, Enum):
    """The availability of the animated thumbnail.

    Option descriptions:
     * ``cancelled`` - The animated thumbnail's creation has been cancelled.
     * ``completed`` - The animated thumbnail has been created.
     * ``failed`` - The animated thumbnail's creation has failed.
     * ``started`` - The animated thumbnail's creation has started."""

    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"
    STARTED = "started"

    __str__ = str.__str__


Status10OrStr: TypeAlias = Annotated[Status10 | str, open_enum_validator(Status10)]
