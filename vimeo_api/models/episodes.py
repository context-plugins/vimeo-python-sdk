from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .buy1 import Buy1, Buy1Dict
from .rent1 import Rent1, Rent1Dict


class Episodes(SdkBaseModel):
    """Information about the On Demand page's episodes, if the page is for a series."""

    buy: Buy1
    rent: Rent1


class EpisodesDict(TypedDict):
    buy: Buy1Dict
    rent: Rent1Dict
