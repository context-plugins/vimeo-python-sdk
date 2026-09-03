from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed4(str, Enum):
    """The event's embed permission setting.

    Option descriptions:
     * ``private`` - The event can't be embedded on any domain.
     * ``public`` - The event can be embedded on any domain.
     * ``whitelist`` - The event can be embedded on permitted domains only."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


Embed4OrStr: TypeAlias = Annotated[Embed4 | str, open_enum_validator(Embed4)]
