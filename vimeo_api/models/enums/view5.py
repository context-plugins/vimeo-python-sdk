from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class View5(str, Enum):
    """Who can access the group.

    Option descriptions:
     * ``anybody`` - Anyone can access the group. This privacy setting appears as ``Public`` on the Vimeo front end.
     * ``members`` - Only group members can access the group."""

    ANYBODY = "anybody"
    MEMBERS = "members"

    __str__ = str.__str__


View5OrStr: TypeAlias = Annotated[View5 | str, open_enum_validator(View5)]
