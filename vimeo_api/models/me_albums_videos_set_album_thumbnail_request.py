from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MeAlbumsVideosSetAlbumThumbnailRequest(SdkBaseModel):
    time_code: Optional[float] = UNSET
    """The time in seconds of the video frame to use as the thumbnail image."""


class MeAlbumsVideosSetAlbumThumbnailRequestDict(TypedDict):
    time_code: NotRequired[float]
