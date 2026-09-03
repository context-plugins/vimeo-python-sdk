from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type17(str, Enum):
    """The project item type.

    Option descriptions:
     * ``folder`` - The project item is a folder.
     * ``live_event`` - The project item is an event.
     * ``showcase`` - The project item is a showcase.
     * ``video`` - The project item is a video."""

    FOLDER = "folder"
    LIVE_EVENT = "live_event"
    SHOWCASE = "showcase"
    VIDEO = "video"

    __str__ = str.__str__


Type17OrStr: TypeAlias = Annotated[Type17 | str, open_enum_validator(Type17)]
