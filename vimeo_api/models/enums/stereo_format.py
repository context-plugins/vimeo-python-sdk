from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StereoFormat(str, Enum):
    """The video's 360 stereo format.

    Option descriptions:
     * ``left-right`` - The stereo format is left-right.
     * ``mono`` - The audio is monaural.
     * ``top-bottom`` - The stereo format is top-bottom."""

    LEFT_RIGHT = "left-right"
    MONO = "mono"
    TOP_BOTTOM = "top-bottom"

    __str__ = str.__str__


StereoFormatOrStr: TypeAlias = Annotated[StereoFormat | str, open_enum_validator(StereoFormat)]
