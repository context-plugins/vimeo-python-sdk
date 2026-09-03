from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comment2(str, Enum):
    """Who can comment on the group.

    Option descriptions:
     * ``all`` - Anyone can comment on the group.
     * ``members`` - Only group members can comment on the group."""

    ALL = "all"
    MEMBERS = "members"

    __str__ = str.__str__


Comment2OrStr: TypeAlias = Annotated[Comment2 | str, open_enum_validator(Comment2)]
