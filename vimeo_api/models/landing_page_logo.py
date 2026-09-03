from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type14 import Type14OrStr


class LandingPageLogo(SdkBaseModel):
    """The navbar logo configuration of the event landing page, or ``null`` when the event was never configured (default
    rendering)."""

    type_: Type14OrStr = Field(alias="type")
    """Which logo to show in the landing page navbar.

    Option descriptions:
     * ``custom`` - A custom brand-kit logo (see ``uri``/``url``).
     * ``none`` - No logo is shown.
     * ``vimeo`` - The Vimeo logo."""

    uri: str | None
    """Brand-kit logo resource URI (custom only)."""

    url: str | None
    """Brand-kit logo image URL (custom only)."""


class LandingPageLogoDict(TypedDict):
    type_: Type14OrStr
    uri: str | None
    url: str | None
