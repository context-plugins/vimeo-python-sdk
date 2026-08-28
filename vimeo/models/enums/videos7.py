from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Videos7(str, Enum):
    """Who can add videos to the group.

    Option descriptions:
     * ``all`` - Anyone can add videos to the group.
     * ``members`` - Only group members can add videos to the group."""

    ALL = "all"
    MEMBERS = "members"

    __str__ = str.__str__


Videos7OrStr: TypeAlias = Annotated[Videos7 | str, open_enum_validator(Videos7)]
