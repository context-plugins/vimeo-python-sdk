from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type32 import Type32OrStr


class LandingPageLogo2(SdkBaseModel):
    """The navbar logo configuration of the event landing page."""

    type_: Optional[Type32OrStr] = Field(default=UNSET, alias="type")
    """Which logo to show in the landing page navbar.

    Option descriptions:
     * ``custom`` - A custom brand-kit logo (see ``uri``).
     * ``none`` - No logo is shown.
     * ``vimeo`` - The Vimeo logo."""

    uri: Optional[str] = UNSET
    """Brand-kit logo resource URI. Required when ``type`` is ``custom``. The display URL is derived server-side from
    this URI."""


class LandingPageLogo2Dict(TypedDict):
    type_: NotRequired[Type32OrStr]
    uri: NotRequired[str]
