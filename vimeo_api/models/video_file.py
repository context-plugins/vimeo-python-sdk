from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.codec import CodecOrStr
from .enums.quality import QualityOrStr
from .enums.rendition import RenditionOrStr
from .enums.type3 import Type3OrStr
from .log import Log, LogDict


class VideoFile(SdkBaseModel):
    codec: CodecOrStr | None
    """The codec of the video file.

    Option descriptions:
     * ``AV1`` - The codec is AV1.
     * ``H264`` - The codec is H264.
     * ``HEVC`` - The codec is HEVC.
     * ``aac`` - The audio codec is AAC."""

    created_time: str
    """The time in ISO 8601 format when the video file was created."""

    expires: Optional[str] = UNSET
    """The time in ISO 8601 format when the video file expires."""

    fps: float
    """The frames per second of the video. Returns 0 for audio-only files."""

    height: float
    """The height of the video in pixels."""

    link: str
    """The direct link to the video file."""

    log: Optional[Log] = UNSET
    md5: str
    """The MD5 hash of the video file."""

    public_name: str
    """The public name of the video file."""

    quality: QualityOrStr
    """The video quality as determined by height and width.

    Option descriptions:
     * ``audio`` - The file is audio-only.
     * ``hd`` - The video is in high definition.
     * ``hls`` - The video is suitable for HTTP live streaming.
     * ``mobile`` - The video is mobile quality.
     * ``sd`` - The video is in standard definition.
     * ``source`` - The video's source file.
     * ``uhd`` - The video resolution is 2K or higher."""

    rendition: RenditionOrStr
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
     * ``1080p`` - The video has 1080p resolution.
     * ``adaptive`` - The video rendition is adaptive (for example, HLS or DASH).
     * ``audio`` - The file is audio-only.
     * ``source`` - The video is the source file."""

    size: float
    """The approximate size in bytes of the video file."""

    size_short: str
    """The converted size of the video file rounded to two decimal places."""

    source_link: Optional[str] = UNSET
    """The source link of the video file."""

    type_: Type3OrStr | None = Field(alias="type")
    """The type of video file.

    Option descriptions:
     * ``audio/mp4`` - The file is an audio-only MPEG-4 container.
     * ``source`` - The video file is a source file.
     * ``video/mp4`` - The video file is in MP4 format.
     * ``video/webm`` - The video file is in WebM format.
     * ``vp6/x-video`` - The video file is in VP6 format."""

    width: float
    """The width of the video in pixels."""


class VideoFileDict(TypedDict):
    codec: CodecOrStr | None
    created_time: str
    expires: NotRequired[str]
    fps: float
    height: float
    link: str
    log: NotRequired[Log | LogDict]
    md5: str
    public_name: str
    quality: QualityOrStr
    rendition: RenditionOrStr
    size: float
    size_short: str
    source_link: NotRequired[str]
    type_: Type3OrStr | None
    width: float
