from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OutroType(str, Enum):
    """The type of the video outro.

    Option descriptions:
     * ``beginning`` - The outro is a thumbnail.
     * ``custom`` - The outro is custom.
     * ``email`` - The outro is an email form.
     * ``image`` - The outro is an image.
     * ``link`` - The outro is a link.
     * ``loop`` - The outro is a loop.
     * ``nothing`` - There is no outro.
     * ``share`` - The outro is a share button.
     * ``text`` - The outro is text.
     * ``threevideos`` - The outro is three video suggestions.
     * ``videos`` - The outro is video suggestions."""

    BEGINNING = "beginning"
    CUSTOM = "custom"
    EMAIL = "email"
    IMAGE = "image"
    LINK = "link"
    LOOP = "loop"
    NOTHING = "nothing"
    SHARE = "share"
    TEXT = "text"
    THREEVIDEOS = "threevideos"
    VIDEOS = "videos"

    __str__ = str.__str__


OutroTypeOrStr: TypeAlias = Annotated[OutroType | str, open_enum_validator(OutroType)]
