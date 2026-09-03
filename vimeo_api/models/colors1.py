from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Colors1(SdkBaseModel):
    """A collection of information about the colors in the video page player."""

    color_four: Optional[str] = UNSET
    """The fourth player color, which controls the player background color."""

    color_one: Optional[str] = UNSET
    """The first player color, which controls the color of the progress bar, buttons, and more."""

    color_three: Optional[str] = UNSET
    """The third player color, which controls the color of text and icons."""

    color_two: Optional[str] = UNSET
    """The second player color, which controls the player accent color."""


class Colors1Dict(TypedDict):
    color_four: NotRequired[str]
    color_one: NotRequired[str]
    color_three: NotRequired[str]
    color_two: NotRequired[str]
