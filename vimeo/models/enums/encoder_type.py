from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EncoderType(str, Enum):
    """The protocol used for this session.

    Option descriptions:
     * ``dash`` - The protocol is DASH.
     * ``rtmp`` - The protocol is RTMP.
     * ``simple_live`` - The protocol is Simplelive.
     * ``srt`` - The protocol is SRT.
     * ``studio_cloud`` - The protocol is StudioCloud.
     * ``unknown`` - The protocol is unknown or not set.
     * ``webrtc`` - The protocol is WebRTC."""

    DASH = "dash"
    RTMP = "rtmp"
    SIMPLE_LIVE = "simple_live"
    SRT = "srt"
    STUDIO_CLOUD = "studio_cloud"
    UNKNOWN = "unknown"
    WEBRTC = "webrtc"

    __str__ = str.__str__


EncoderTypeOrStr: TypeAlias = Annotated[EncoderType | str, open_enum_validator(EncoderType)]
