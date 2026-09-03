from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EventType(str, Enum):
    """The type of event.

    Option descriptions:
     * ``default`` - The event type is a regular recurring event.
     * ``venue`` - The event type is a venue."""

    DEFAULT = "default"
    VENUE = "venue"

    __str__ = str.__str__


EventTypeOrStr: TypeAlias = Annotated[EventType | str, open_enum_validator(EventType)]
