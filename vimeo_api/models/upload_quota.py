from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .lifetime import Lifetime, LifetimeDict
from .periodic import Periodic, PeriodicDict
from .restricted import Restricted, RestrictedDict
from .space import Space, SpaceDict


class UploadQuota(SdkBaseModel):
    """The upload quota. This information appears only when the authenticated user has upload access and is looking at
    their own user record."""

    lifetime: Lifetime
    """Information about the authenticated user's lifetime upload usage."""

    periodic: Periodic
    """Information about the authenticated user's usage for the current period."""

    recently_deleted_disk_space: float
    """The number of bytes used by videos currently in the Recently Deleted folder."""

    restricted: Restricted
    """The restricted video storage quota (for embeddable and private videos)."""

    space: Space
    """Information about the authenticated user's upload space remaining for the current period."""


class UploadQuotaDict(TypedDict):
    lifetime: LifetimeDict
    periodic: PeriodicDict
    recently_deleted_disk_space: float
    restricted: RestrictedDict
    space: SpaceDict
