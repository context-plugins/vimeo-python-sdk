from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsVideosRequest1(SdkBaseModel):
    video_uri: str
    """A member of an array representing the URIs of the videos to add. For each member in the array, use the format
    ``{"video_uri":"x"}`` where **x** is a video URI. For more information on batch requests like this, see `Using
    Common Formats and Parameters <https://developer.vimeo.com/api/common-formats#working-with-batch-requests>`__."""


class ChannelsVideosRequest1Dict(TypedDict):
    video_uri: str
