from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type40(str, Enum):
    """The end screen type.

    Option descriptions:
     * ``empty`` - The end screen is empty.
     * ``loop`` - The end screen loops the video playback.
     * ``share`` - The end screen includes sharing options.
     * ``thumbnail`` - The end screen includes the thumbnail of the video."""

    EMPTY = "empty"
    LOOP = "loop"
    SHARE = "share"
    THUMBNAIL = "thumbnail"

    __str__ = str.__str__


Type40OrStr: TypeAlias = Annotated[Type40 | str, open_enum_validator(Type40)]
