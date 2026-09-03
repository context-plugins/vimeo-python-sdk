from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RegionalDelivery(SdkBaseModel):
    display_description: str
    """The translated display description of the regional delivery permission policy."""

    display_name: str
    """The translated display name of the regional delivery permission policy."""

    name: str
    """The name of the regional delivery permission policy."""


class RegionalDeliveryDict(TypedDict):
    display_description: str
    display_name: str
    name: str
