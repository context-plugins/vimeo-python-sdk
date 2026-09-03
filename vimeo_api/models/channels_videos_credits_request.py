from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsVideosCreditsRequest(SdkBaseModel):
    email: str
    """The email address of the credited person."""

    name: str
    """The name of the credited person."""

    role: str
    """The role of the credited person."""

    user_uri: str
    """The Vimeo URI of the credited person."""


class ChannelsVideosCreditsRequestDict(TypedDict):
    email: str
    name: str
    role: str
    user_uri: str
