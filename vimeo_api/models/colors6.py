from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Colors6(SdkBaseModel):
    color_four: Optional[str] = UNSET
    """The hexadecimal color code of the fourth player color, which controls the player background color."""

    color_one: Optional[str] = UNSET
    """The hexadecimal color code of the first player color, which controls the color of the progress bar, buttons, and
    more."""

    color_three: Optional[str] = UNSET
    """The hexadecimal color code of the third player color, which controls the color of text and icons."""

    color_two: Optional[str] = UNSET
    """The hexadecimal color code of the second player color, which controls the player accent color."""


class Colors6Dict(TypedDict):
    color_four: NotRequired[str]
    color_one: NotRequired[str]
    color_three: NotRequired[str]
    color_two: NotRequired[str]
