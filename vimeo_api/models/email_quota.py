from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EmailQuota(SdkBaseModel):
    """Information about the event owner's email quota."""

    capping: float
    """The maximum number of entity emails that the user can send."""

    total: float
    """The current number of entity emails that the user has sent."""


class EmailQuotaDict(TypedDict):
    capping: float
    total: float
