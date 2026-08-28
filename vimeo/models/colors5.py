from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Colors5(SdkBaseModel):
    color_four: str
    """The fourth player color, which controls the player background color."""

    color_one: str
    """The first player color, which controls the color of the progress bar, buttons, and more."""

    color_three: str
    """The third player color, which controls the color of text and icons."""

    color_two: str
    """The second player color, which controls the player accent color. _This field is identical to **color**._"""


class Colors5Dict(TypedDict):
    color_four: str
    color_one: str
    color_three: str
    color_two: str
