from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsModeratorsRequest(SdkBaseModel):
    user_uri: str
    """The URI of a user to remove as a moderator."""


class ChannelsModeratorsRequestDict(TypedDict):
    user_uri: str
