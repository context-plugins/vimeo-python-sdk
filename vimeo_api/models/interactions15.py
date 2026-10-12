from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .purchase import Purchase, PurchaseDict


class Interactions15(SdkBaseModel):
    purchase: Purchase


class Interactions15Dict(TypedDict):
    purchase: PurchaseDict
