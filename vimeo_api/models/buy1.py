from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Buy1(SdkBaseModel):
    active: bool
    """Whether all the videos on the On Demand page can be purchased as a whole."""

    price: float | None
    """The default price to buy an episode."""


class Buy1Dict(TypedDict):
    active: bool
    price: float | None
