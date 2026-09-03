from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.name1 import Name1OrStr
from .enums.owner2 import Owner2OrStr
from .enums.portrait2 import Portrait2OrStr


class Title2(SdkBaseModel):
    name: Optional[Name1OrStr] = UNSET
    """How to handle the video title in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the video title.
     * ``show`` - Show the video title.
     * ``user`` - Enable the user to decide."""

    owner: Optional[Owner2OrStr] = UNSET
    """How to handle the owner information in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the owner info.
     * ``show`` - Show the owner info.
     * ``user`` - Enable the user to decide."""

    portrait: Optional[Portrait2OrStr] = UNSET
    """How to handle the owner portrait in the title bar of the embeddable player.

    Option descriptions:
     * ``hide`` - Hide the portrait.
     * ``show`` - Show the portrait.
     * ``user`` - Enable the user to decide."""


class Title2Dict(TypedDict):
    name: NotRequired[Name1OrStr]
    owner: NotRequired[Owner2OrStr]
    portrait: NotRequired[Portrait2OrStr]
