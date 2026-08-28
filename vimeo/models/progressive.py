from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.codec1 import Codec1OrStr
from .enums.rendition1 import Rendition1OrStr
from .enums.type6 import Type6OrStr


class Progressive(SdkBaseModel):
    codec: Codec1OrStr | None
    """The codec of the video file.

    Option descriptions:
     * ``AV1`` - The codec is AV1.
     * ``H264`` - The codec is H264.
     * ``HEVC`` - The codec is HEVC."""

    created_time: str
    """The time in ISO 8601 format when the video file was created."""

    fps: float
    """The frames per second of the video."""

    height: float | None
    """The height of the video in pixels."""

    link: str
    """The direct link to the video file."""

    link_expiration_time: str
    """The time in ISO 8601 format when the link to the video file expires."""

    log: Optional[Any] = UNSET
    """The URLs for logging events."""

    md5: str
    """The MD5 hash of the video file."""

    rendition: Rendition1OrStr
    """The video rendition.

    Option descriptions:
     * ``2k`` - The video has 2K resolution.
     * ``4k`` - The video has 4K resolution.
     * ``5k`` - The video has 5K resolution.
     * ``6k`` - The video has 6K resolution.
     * ``7k`` - The video has 7K resolution.
     * ``8k`` - The video has 8K resolution.
     * ``240p`` - The video has 240p resolution.
     * ``360p`` - The video has 360p resolution.
     * ``480p`` - The video has 480p resolution.
     * ``540p`` - The video has 540p resolution.
     * ``720p`` - The video has 720p resolution.
     * ``1080p`` - The video has 1080p resolution."""

    size: float | None
    """The size in bytes of the video file."""

    type_: Type6OrStr | None = Field(alias="type")
    """The type of video file.

    Option descriptions:
     * ``source`` - The video file is a source file.
     * ``video/mp4`` - The video file is in MP4 format.
     * ``video/webm`` - The video file is in WebM format.
     * ``vp6/x-video`` - The video file is in VP6 format."""

    width: float | None
    """The width of the video in pixels."""


class ProgressiveDict(TypedDict):
    codec: Codec1OrStr | None
    created_time: str
    fps: float
    height: float | None
    link: str
    link_expiration_time: str
    log: NotRequired[Any]
    md5: str
    rendition: Rendition1OrStr
    size: float | None
    type_: Type6OrStr | None
    width: float | None
