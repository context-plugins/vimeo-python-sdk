from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsVideosRequest(SdkBaseModel):
    video_uri: str
    """The URI of a video to remove."""


class ChannelsVideosRequestDict(TypedDict):
    video_uri: str
