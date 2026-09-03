from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Embed1(str, Enum):
    """The video's embed permission setting.

    Option descriptions:
     * ``private`` - The video is private.
     * ``public`` - Anyone can embed the video.
     * ``whitelist`` - The video can be embedded on specific domains."""

    PRIVATE = "private"
    PUBLIC = "public"
    WHITELIST = "whitelist"

    __str__ = str.__str__


Embed1OrStr: TypeAlias = Annotated[Embed1 | str, open_enum_validator(Embed1)]
