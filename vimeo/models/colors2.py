from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Colors2(SdkBaseModel):
    """The first and second colors of the On Demand page."""

    primary: str
    """The hexadecimal color code for the On Demand page's first color."""

    secondary: str
    """The hexadecimal color code for the On Demand page's second color."""


class Colors2Dict(TypedDict):
    primary: str
    secondary: str
