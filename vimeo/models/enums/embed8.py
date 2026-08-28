from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed8(str, Enum):
    """The embed permission level for the event.

    Option descriptions:
     * ``private`` - Only the user can embed the event.
     * ``public`` - Anyone can embed the event.
     * ``whitelist`` - Only specified users can embed the event."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


Embed8OrStr: TypeAlias = Annotated[Embed8 | str, open_enum_validator(Embed8)]
