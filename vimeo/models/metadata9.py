from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections9 import Connections9, Connections9Dict
from .purchase_interaction import PurchaseInteraction, PurchaseInteractionDict


class Metadata9(SdkBaseModel):
    """Metadata about the On Demand page."""

    connections: Connections9
    """A collection of information that is connected to this resource, including videos, genres, and pictures
    connections."""

    interactions: PurchaseInteraction
    """The user's available purchase interactions."""


class Metadata9Dict(TypedDict):
    connections: Connections9 | Connections9Dict
    interactions: PurchaseInteraction | PurchaseInteractionDict
