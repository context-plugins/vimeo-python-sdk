from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Quality(str, Enum):
    """The video quality as determined by height and width.

    Option descriptions:
     * ``audio`` - The file is audio-only.
     * ``hd`` - The video is in high definition.
     * ``hls`` - The video is suitable for HTTP live streaming.
     * ``mobile`` - The video is mobile quality.
     * ``sd`` - The video is in standard definition.
     * ``source`` - The video's source file.
     * ``uhd`` - The video resolution is 2K or higher."""

    AUDIO = "audio"
    HD = "hd"
    HLS = "hls"
    MOBILE = "mobile"
    SD = "sd"
    SOURCE = "source"
    UHD = "uhd"

    __str__ = str.__str__


QualityOrStr: TypeAlias = Annotated[Quality | str, open_enum_validator(Quality)]
