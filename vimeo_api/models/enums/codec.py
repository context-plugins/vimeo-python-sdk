from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Codec(str, Enum):
    """The codec of the video file.

    Option descriptions:
     * ``AV1`` - The codec is AV1.
     * ``H264`` - The codec is H264.
     * ``HEVC`` - The codec is HEVC.
     * ``aac`` - The audio codec is AAC."""

    AV1 = "AV1"
    H264 = "H264"
    HEVC = "HEVC"
    AAC = "aac"

    __str__ = str.__str__


CodecOrStr: TypeAlias = Annotated[Codec | str, open_enum_validator(Codec)]
