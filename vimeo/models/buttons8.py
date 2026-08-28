from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Buttons8(SdkBaseModel):
    embed: Optional[bool] = UNSET
    """Whether to show the button for embeds on the embeddable player."""

    fullscreen: Optional[bool] = UNSET
    """Whether to show the button for fullscreen mode on the embeddable player."""

    hd: Optional[bool] = UNSET
    """Whether to show the button for HD video on the embeddable player."""

    like: Optional[bool] = UNSET
    """Whether to show the button for likes on the embeddable player."""

    scaling: Optional[bool] = UNSET
    """Whether to show the button for scaling on the embeddable player in fullscreen mode."""

    share: Optional[bool] = UNSET
    """Whether to show the button for shares on the embeddable player."""

    watchlater: Optional[bool] = UNSET
    """Whether to show the button for watching later on the embeddable player."""


class Buttons8Dict(TypedDict):
    embed: NotRequired[bool]
    fullscreen: NotRequired[bool]
    hd: NotRequired[bool]
    like: NotRequired[bool]
    scaling: NotRequired[bool]
    share: NotRequired[bool]
    watchlater: NotRequired[bool]
