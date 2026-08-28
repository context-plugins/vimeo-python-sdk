from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .entitlements import Entitlements, EntitlementsDict
from .interactions15 import Interactions15, Interactions15Dict
from .purchased_product import PurchasedProduct, PurchasedProductDict


class Metadata25(SdkBaseModel):
    """The URLs and entitlements of the associated products in the store."""

    entitlements: Entitlements
    """The URLs and entitlements of the associated products in the store."""

    interactions: Interactions15
    is_bandwidth_product: bool
    """Whether the product is a bandwidth product."""

    is_ps_plan: bool
    """Whether the product is a Vimeo payments service product."""

    purchased_product: PurchasedProduct
    """Information about the purchased product."""


class Metadata25Dict(TypedDict):
    entitlements: Entitlements | EntitlementsDict
    interactions: Interactions15 | Interactions15Dict
    is_bandwidth_product: bool
    is_ps_plan: bool
    purchased_product: PurchasedProduct | PurchasedProductDict
