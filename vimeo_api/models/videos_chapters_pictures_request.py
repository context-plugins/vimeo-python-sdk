from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosChaptersPicturesRequest(SdkBaseModel):
    timecode: Optional[float] = UNSET
    """The timecode, given in seconds from the start of the video, indicating when the thumbnail should be generated
    from the video."""


class VideosChaptersPicturesRequestDict(TypedDict):
    timecode: NotRequired[float]
