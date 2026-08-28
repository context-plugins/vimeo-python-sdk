from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeAlbumsVideosRequest(SdkBaseModel):
    videos: str
    """A comma-separated list of video URIs corresponding to the videos to add."""


class MeAlbumsVideosRequestDict(TypedDict):
    videos: str
