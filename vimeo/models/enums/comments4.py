from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comments4(str, Enum):
    """Who can comment on the user's video uploads by default.

    Option descriptions:
     * ``anybody`` - Anyone can comment.
     * ``contacts`` - Only the user's contacts can comment.
     * ``nobody`` - No one can comment."""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    NOBODY = "nobody"

    __str__ = str.__str__


Comments4OrStr: TypeAlias = Annotated[Comments4 | str, open_enum_validator(Comments4)]
