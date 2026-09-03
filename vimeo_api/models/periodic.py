from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.period3 import Period3OrStr
from .enums.unit import UnitOrStr


class Periodic(SdkBaseModel):
    """Information about the authenticated user's usage for the current period."""

    free: float | None
    """The number of bytes or video count remaining in the authenticated user's upload quota for the current period."""

    max: float | None
    """The total number of bytes or videos that the authenticated user can upload per period."""

    period: Period3OrStr | None
    """The renewal frequency of the quota.

    Option descriptions:
     * ``lifetime`` - The user doesn't have a periodic quota.
     * ``month`` - The quota renews monthly.
     * ``week`` - The quota renews weekly.
     * ``year`` - The quota renews yearly."""

    reset_date: str | None
    """The time in ISO 8601 format when the authenticated user's upload quota resets."""

    unit: UnitOrStr | None
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_count`` - The quota is calculated using the count of the videos.
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    used: float | None
    """The number of bytes or video count that the authenticated user has already uploaded against their quota in the
    current period."""


class PeriodicDict(TypedDict):
    free: float | None
    max: float | None
    period: Period3OrStr | None
    reset_date: str | None
    unit: UnitOrStr | None
    used: float | None
