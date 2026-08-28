from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type7(str, Enum):
    """The type of the video.

    Option descriptions:
     * ``live`` - The video is or was an event.
     * ``stock`` - The video is a Vimeo Stock video.
     * ``video`` - The video is a standard Vimeo video."""

    LIVE = "live"
    STOCK = "stock"
    VIDEO = "video"

    __str__ = str.__str__


Type7OrStr: TypeAlias = Annotated[Type7 | str, open_enum_validator(Type7)]
