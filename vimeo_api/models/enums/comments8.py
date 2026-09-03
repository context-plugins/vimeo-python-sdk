from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Comments8(str, Enum):
    """The privacy level required to comment on the video.

    Option descriptions:
     * ``anybody`` - Anyone can comment on the video.
     * ``contacts`` - Only the owner's contacts can comment on the video.
     * ``nobody`` - No one can comment on the video."""

    ANYBODY = "anybody"
    CONTACTS = "contacts"
    NOBODY = "nobody"

    __str__ = str.__str__


Comments8OrStr: TypeAlias = Annotated[Comments8 | str, open_enum_validator(Comments8)]
