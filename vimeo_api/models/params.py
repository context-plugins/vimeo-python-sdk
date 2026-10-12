from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ai import Ai, AiDict
from .bandwidth1 import Bandwidth1, Bandwidth1Dict
from .enums.video_storage_quota_period import VideoStorageQuotaPeriodOrStr
from .enums.video_storage_quota_unit import VideoStorageQuotaUnitOrStr
from .seats import Seats, SeatsDict
from .storage import Storage, StorageDict


class Params(SdkBaseModel):
    """The list of entitlement parameters corresponding to the tier."""

    ai: Ai
    """AI credits entitlements information."""

    bandwidth: Bandwidth1
    """Bandwidth entitlement information."""

    restricted_video_storage_limit: str | None
    """The restricted video storage limit for the tier, formatted as a human-readable byte string (e.g. "1GB", "50GB",
    "7TB"). Null means unlimited."""

    seats: Seats
    """Team seats entitlement information."""

    storage: Storage
    """Video storage entitlement information."""

    team_seats: float | None
    """The number of team seats included with the tier for the monthly plan."""

    video_storage_periodic_quota: str | None
    """The amount of video storage for the user's periodic quota for the annual plan."""

    video_storage_quota_cap: str | None
    """The video storage total lifetime cap for the annual plan."""

    video_storage_quota_period: VideoStorageQuotaPeriodOrStr
    """The video storage quota period for the annual plan.

    Option descriptions:
     * ``lifetime`` - The product has a lifetime video storage quota period.
     * ``month`` - The product has a monthly video storage quota period.
     * ``week`` - The product has a weekly video storage quota period.
     * ``year`` - The product has a yearly video storage quota period."""

    video_storage_quota_unit: VideoStorageQuotaUnitOrStr
    """The unit of the video storage for the user's periodic quota for the annual plan.

    Option descriptions:
     * ``video_count`` - The product has video storage based on video count.
     * ``video_size`` - The product has video storage based on video size."""


class ParamsDict(TypedDict):
    ai: AiDict
    bandwidth: Bandwidth1Dict
    restricted_video_storage_limit: str | None
    seats: SeatsDict
    storage: StorageDict
    team_seats: float | None
    video_storage_periodic_quota: str | None
    video_storage_quota_cap: str | None
    video_storage_quota_period: VideoStorageQuotaPeriodOrStr
    video_storage_quota_unit: VideoStorageQuotaUnitOrStr
