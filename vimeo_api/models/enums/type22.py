from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type22(str, Enum):
    """The preset outro type.

    Option descriptions:
     * ``link`` - The outro includes a link.
     * ``no idea`` - The outro type is ``no idea``. The outro includes uploaded videos.
     * ``text`` - The outro includes text.
     * ``uploaded_clips`` - The outro includes uploaded videos.
     * ``uploaded_videos`` - The outro includes uploaded videos."""

    LINK = "link"
    NO_IDEA = "no idea"
    TEXT = "text"
    UPLOADED_CLIPS = "uploaded_clips"
    UPLOADED_VIDEOS = "uploaded_videos"

    __str__ = str.__str__


Type22OrStr: TypeAlias = Annotated[Type22 | str, open_enum_validator(Type22)]
