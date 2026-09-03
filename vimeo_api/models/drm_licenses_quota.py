from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.period2 import Period2OrStr


class DrmLicensesQuota(SdkBaseModel):
    """Information about the user's DRM usage quota."""

    available: Optional[float] = UNSET
    """The maximum number of DRM sessions granted to the authenticated user."""

    period: Optional[Period2OrStr] = UNSET
    """The time period for which the DRM usage activity is evaluated.

    Option descriptions:
     * ``lifetime`` - The quota period is for the lifetime of the account.
     * ``year`` - The quota period is one year."""

    remaining: Optional[float] = UNSET
    """The number of DRM sessions that are remaining for the authenticated user."""

    reset_date: Optional[str] = UNSET
    """The date of the user's next DRM sessions reset."""

    used: Optional[float] = UNSET
    """The number of DRM sessions that have been consumed."""


class DrmLicensesQuotaDict(TypedDict):
    available: NotRequired[float]
    period: NotRequired[Period2OrStr]
    remaining: NotRequired[float]
    reset_date: NotRequired[str]
    used: NotRequired[float]
