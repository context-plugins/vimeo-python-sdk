from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.privacy8 import Privacy8OrStr


class ChannelsRequest1(SdkBaseModel):
    description: Optional[str] = UNSET
    """The description of the channel."""

    link: Optional[str] = UNSET
    """The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in
    ``/channels/{url_custom}``. Submitting ``""`` for this field removes the link alias."""

    name: Optional[str] = UNSET
    """The name of the channel."""

    privacy: Optional[Privacy8OrStr] = UNSET
    """The privacy level of the channel.

    Option descriptions:
     * ``anybody`` - Anyone can access the channel.
     * ``moderators`` - Only moderators can access the channel.
     * ``users`` - Only moderators and designated users can access the channel."""


class ChannelsRequest1Dict(TypedDict):
    description: NotRequired[str]
    link: NotRequired[str]
    name: NotRequired[str]
    privacy: NotRequired[Privacy8OrStr]
