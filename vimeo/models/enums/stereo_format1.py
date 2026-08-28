from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class StereoFormat1(str, Enum):
    """The 360 spatial stereo format.

    Option descriptions:
     * ``left-right`` - Use left-right stereo.
     * ``mono`` - Use monaural audio.
     * ``top-bottom`` - Use top-bottom stereo."""

    LEFT_RIGHT = "left-right"
    MONO = "mono"
    TOP_BOTTOM = "top-bottom"

    __str__ = str.__str__


StereoFormat1OrStr: TypeAlias = Annotated[StereoFormat1 | str, open_enum_validator(StereoFormat1)]
