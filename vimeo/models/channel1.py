from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Channel1(SdkBaseModel):
    """Information about removing a video from the channel. This information is included only when the video is
    referenced by the URI of a channel that's moderated by the user."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Channel1Dict(TypedDict):
    options: list[str]
    uri: str
