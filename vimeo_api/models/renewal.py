from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Renewal(SdkBaseModel):
    """Information about the authenticated user's next renewal."""

    display_date: str
    """The date in YYYY-MM-DD format when the authenticated user's membership renews (or expires, if they have disabled
    automatic renewal, or the trial ends without renewal in case of a Reverse trial). This value is for display only;
    the exact time at which renewal or expiration occurs on this date isn't guaranteed."""


class RenewalDict(TypedDict):
    display_date: str
