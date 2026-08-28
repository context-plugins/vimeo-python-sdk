from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .subscribe1 import Subscribe1, Subscribe1Dict


class PurchaseInteraction(SdkBaseModel):
    buy: OptionalNullable[Any] = UNSET
    """Information on purchasing the On Demand video."""

    rent: OptionalNullable[Any] = UNSET
    """Information on renting the On Demand video."""

    subscribe: OptionalNullable[Subscribe1] = UNSET
    """Information on subscribing to the On Demand video."""


class PurchaseInteractionDict(TypedDict):
    buy: NotRequired[Any | None]
    rent: NotRequired[Any | None]
    subscribe: NotRequired[Subscribe1 | Subscribe1Dict | None]
