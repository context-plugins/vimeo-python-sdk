from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.title_font_family import TitleFontFamilyOrStr
from .enums.title_font_weight import TitleFontWeightOrInt
from .logo import Logo, LogoDict


class Customization(SdkBaseModel):
    """The contents of the page customization group (background color, title font, and inline logo)."""

    ambient_backlight: Optional[bool] = UNSET
    """Whether to render the ambient backlight glow behind the video player on the page."""

    background_color: OptionalNullable[str] = UNSET
    """The page background color as a ``#``-prefixed hex string, or null if not set."""

    hide_vimeo_header: Optional[bool] = UNSET
    """Whether to hide the Vimeo header (top navigation bar) on the video page."""

    logo: Optional[Logo] = UNSET
    """Optional logo to display inline with the video title."""

    title_font_family: OptionalNullable[TitleFontFamilyOrStr] = UNSET
    """The selected video title font family."""

    title_font_weight: OptionalNullable[TitleFontWeightOrInt] = UNSET
    """The selected video title font weight.

    Option descriptions:
     * ``300`` - Light
     * ``400`` - Regular
     * ``500`` - Medium
     * ``700`` - Bold"""


class CustomizationDict(TypedDict):
    ambient_backlight: NotRequired[bool]
    background_color: NotRequired[str | None]
    hide_vimeo_header: NotRequired[bool]
    logo: NotRequired[LogoDict]
    title_font_family: NotRequired[TitleFontFamilyOrStr | None]
    title_font_weight: NotRequired[TitleFontWeightOrInt | None]
