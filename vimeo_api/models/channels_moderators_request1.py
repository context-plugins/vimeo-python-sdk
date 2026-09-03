from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsModeratorsRequest1(SdkBaseModel):
    user_uri: str
    """The URI of the user to add as a moderator."""


class ChannelsModeratorsRequest1Dict(TypedDict):
    user_uri: str
