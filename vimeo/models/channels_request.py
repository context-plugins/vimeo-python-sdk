from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.privacy7 import Privacy7OrStr


class ChannelsRequest(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description of the channel."""

    link: Optional[str] = UNSET
    """The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in
    ``/channels/{url_custom}``."""

    name: str
    """The name of the channel."""

    privacy: Privacy7OrStr
    """The privacy level of the channel.

    Option descriptions:
     * ``anybody`` - Anyone can access the channel.
     * ``moderators`` - Only moderators can access the channel.
     * ``user`` - Only moderators and designated users can access the channel."""


class ChannelsRequestDict(TypedDict):
    description: NotRequired[str]
    link: NotRequired[str]
    name: str
    privacy: Privacy7OrStr
