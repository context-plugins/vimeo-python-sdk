from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.credits_period import CreditsPeriodOrStr


class Ai(SdkBaseModel):
    """AI credits entitlements information."""

    credits_period: CreditsPeriodOrStr
    """The quota period unit for the user's AI credits quota.

    Option descriptions:
     * ``month`` - The product has a monthly AI credits quota period.
     * ``week`` - The product has a weekly AI credits quota period.
     * ``year`` - The product has a yearly AI credits quota period."""

    periodic_credits: float | None
    """The number of AI credits for the user's period."""


class AiDict(TypedDict):
    credits_period: CreditsPeriodOrStr
    periodic_credits: float | None
