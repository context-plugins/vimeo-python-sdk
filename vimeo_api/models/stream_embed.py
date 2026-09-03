from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.embed8 import Embed8OrStr


class StreamEmbed(SdkBaseModel):
    embed: Optional[Embed8OrStr] = UNSET
    """The embed permission level for the event.

    Option descriptions:
     * ``private`` - Only the user can embed the event.
     * ``public`` - Anyone can embed the event.
     * ``whitelist`` - Only specified users can embed the event."""


class StreamEmbedDict(TypedDict):
    embed: NotRequired[Embed8OrStr]
