from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Join1(str, Enum):
    """Who can join the group.

    Option descriptions:
     * ``anybody`` - Anyone can join the group.
     * ``members`` - Only people with a Vimeo account can join the group."""

    ANYBODY = "anybody"
    MEMBERS = "members"

    __str__ = str.__str__


Join1OrStr: TypeAlias = Annotated[Join1 | str, open_enum_validator(Join1)]
