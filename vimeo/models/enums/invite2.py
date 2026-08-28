from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Invite2(str, Enum):
    """Who can invite new members to the group.

    Option descriptions:
     * ``all`` - Anyone can invite new members to the group.
     * ``members`` - Only group members can invite new members to the group."""

    ALL = "all"
    MEMBERS = "members"

    __str__ = str.__str__


Invite2OrStr: TypeAlias = Annotated[Invite2 | str, open_enum_validator(Invite2)]
