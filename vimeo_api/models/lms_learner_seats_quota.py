from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LmsLearnerSeatsQuota(SdkBaseModel):
    """Information about the user's learning management system learner seats quota."""

    available: Optional[float] = UNSET
    """The maximum number of learning management system learner seats granted to the authenticated user."""

    used: Optional[float] = UNSET
    """The number of learning management system learner seats already used by the authenticated user."""


class LmsLearnerSeatsQuotaDict(TypedDict):
    available: NotRequired[float]
    used: NotRequired[float]
