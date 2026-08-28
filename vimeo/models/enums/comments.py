from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comments(str, Enum):
    """The authenticated user's privacy preference for comments.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the user's videos.
     * ``contacts`` - Only contacts can comment on the user's videos.
     * ``nobody`` - No one can comment on the user's videos."""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    NOBODY = "nobody"

    __str__ = str.__str__


CommentsOrStr: TypeAlias = Annotated[Comments | str, open_enum_validator(Comments)]
