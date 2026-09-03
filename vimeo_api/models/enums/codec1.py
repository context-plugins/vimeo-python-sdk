from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Codec1(str, Enum):
    """The codec of the video file.

    Option descriptions:
     * ``AV1`` - The codec is AV1.
     * ``H264`` - The codec is H264.
     * ``HEVC`` - The codec is HEVC."""

    AV1 = "AV1"
    H264 = "H264"
    HEVC = "HEVC"

    __str__ = str.__str__


Codec1OrStr: TypeAlias = Annotated[Codec1 | str, open_enum_validator(Codec1)]
