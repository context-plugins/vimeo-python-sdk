from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Privacy8(str, Enum):
    """The privacy level of the channel.

    Option descriptions:
     * ``anybody`` - Anyone can access the channel.
     * ``moderators`` - Only moderators can access the channel.
     * ``users`` - Only moderators and designated users can access the channel."""

    ANYBODY = "anybody"
    MODERATORS = "moderators"
    USERS = "users"

    __str__ = str.__str__


Privacy8OrStr: TypeAlias = Annotated[Privacy8 | str, open_enum_validator(Privacy8)]
