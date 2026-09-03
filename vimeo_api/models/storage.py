from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.quota_period1 import QuotaPeriod1OrStr
from .enums.quota_unit import QuotaUnitOrStr


class Storage(SdkBaseModel):
    """Video storage entitlement information."""

    periodic_quota: str | None
    """The amount of video storage for the user's periodic quota for the annual plan."""

    quota_cap: str | None
    """The video storage total lifetime cap for the annual plan."""

    quota_period: QuotaPeriod1OrStr
    """The video storage quota period for the annual plan.

    Option descriptions:
     * ``lifetime`` - The product has a lifetime video storage quota period.
     * ``month`` - The product has a monthly video storage quota period.
     * ``week`` - The product has a weekly video storage quota period.
     * ``year`` - The product has a yearly video storage quota period."""

    quota_unit: QuotaUnitOrStr
    """The unit of the video storage for the user's periodic quota for the annual plan.

    Option descriptions:
     * ``video_count`` - The product has video storage based on video count.
     * ``video_size`` - The product has video storage based on video size."""


class StorageDict(TypedDict):
    periodic_quota: str | None
    quota_cap: str | None
    quota_period: QuotaPeriod1OrStr
    quota_unit: QuotaUnitOrStr
