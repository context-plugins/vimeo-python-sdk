from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.quota_period import QuotaPeriodOrStr


class Bandwidth1(SdkBaseModel):
    """Bandwidth entitlement information."""

    periodic_quota: str | None
    """The amount of bandwidth for the user's period."""

    quota_period: QuotaPeriodOrStr
    """The quota period unit for the user's bandwidth quota.

    Option descriptions:
     * ``month`` - The product has a monthly bandwidth quota period.
     * ``week`` - The product has a weekly bandwidth quota period.
     * ``year`` - The product has a yearly bandwidth quota period."""


class Bandwidth1Dict(TypedDict):
    periodic_quota: str | None
    quota_period: QuotaPeriodOrStr
