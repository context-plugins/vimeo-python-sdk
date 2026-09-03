from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type34(str, Enum):
    """The end screen type.

    Option descriptions:
     * ``beginning`` - The end screen is a thumbnail.
     * ``custom`` - The end screen is custom.
     * ``email`` - The end screen is an email form.
     * ``image`` - The end screen is an image.
     * ``link`` - The end screen is a link.
     * ``loop`` - The end screen is a loop.
     * ``nothing`` - There is no end screen.
     * ``share`` - The end screen is a share button.
     * ``text`` - The end screen is text.
     * ``threevideos`` - The end screen is three video suggestions.
     * ``videos`` - The end screen is video suggestions."""

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


Type34OrStr: TypeAlias = Annotated[Type34 | str, open_enum_validator(Type34)]
