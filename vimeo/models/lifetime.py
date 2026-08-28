from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.unit import UnitOrStr


class Lifetime(SdkBaseModel):
    """Information about the authenticated user's lifetime upload usage."""

    free: float | None
    """The number of bytes or videos remaining in the authenticated user's lifetime maximum."""

    max: float | None
    """The total number of bytes or videos that the authenticated user can upload across the lifetime of their
    account."""

    unit: UnitOrStr | None
    """The unit that's used to compute quota.

    Option descriptions:
     * ``video_count`` - The quota is calculated using the count of the videos.
     * ``video_size`` - The quota is calculated using the byte size of the videos."""

    used: float | None
    """The number of bytes or videos that the authenticated user has already uploaded against their lifetime limit."""


class LifetimeDict(TypedDict):
    free: float | None
    max: float | None
    unit: UnitOrStr | None
    used: float | None
