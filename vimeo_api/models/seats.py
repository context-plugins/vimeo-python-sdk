from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.mode import ModeOrStr


class Seats(SdkBaseModel):
    """Team seats entitlement information."""

    admin: float | None
    """The number of admin team seats included with the tier."""

    authenticated: float | None
    """The number of authenticated team seats included with the tier."""

    mode: ModeOrStr
    """The team seats mode for the user's team.

    Option descriptions:
     * ``admin_and_authenticated`` - The mode for Enterprise-Base Platform, Enterprise-Marketing, and Enterprise-Central
            users.
     * ``global`` - The default mode for legacy and self-serve users.
     * ``per_seat_type`` - The mode for sales-assisted users, including Enterprise, Custom, and Custom OTT."""

    team: float | None
    """The number of team seats included with the tier for the monthly plan."""


class SeatsDict(TypedDict):
    admin: float | None
    authenticated: float | None
    mode: ModeOrStr
    team: float | None
