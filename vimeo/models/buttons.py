from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Buttons(SdkBaseModel):
    """A collection of information about the buttons that appear on the interface of the embeddable player."""

    embed: bool
    """Whether the button for embeds appears in the embeddable player."""

    fullscreen: bool
    """Whether the button for fullscreen mode appears in the embeddable player."""

    hd: bool
    """Whether the button for HD videos appears in the embeddable player."""

    like: bool
    """Whether the button for likes appears in the embeddable player."""

    reaction: Optional[bool] = UNSET
    """Whether the button for reactions appears in the embeddable player."""

    scaling: bool
    """Whether the button for scaling appears in the embeddable player."""

    share: bool
    """Whether the button for shares appears in the embeddable player."""

    watchlater: bool
    """Whether the button for watching later appears in the embeddable player."""


class ButtonsDict(TypedDict):
    embed: bool
    fullscreen: bool
    hd: bool
    like: bool
    reaction: NotRequired[bool]
    scaling: bool
    share: bool
    watchlater: bool
