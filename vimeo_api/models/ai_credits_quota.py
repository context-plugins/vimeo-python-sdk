from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .balance import Balance, BalanceDict
from .enums.period import PeriodOrStr


class AiCreditsQuota(SdkBaseModel):
    """Information about the user's AI credits quota."""

    available: Optional[float] = UNSET
    """The maximum number of AI credits granted to the authenticated user."""

    balances: Optional[list[Balance]] = UNSET
    """An array of objects listing the balances and expiration dates for the user's AI credits quota."""

    period: Optional[PeriodOrStr] = UNSET
    """The time period for which the AI credit activity is evaluated.

    Option descriptions:
     * ``lifetime`` - The quota period is for the lifetime of the account.
     * ``month`` - The quota period is one month.
     * ``week`` - The quota period is one week.
     * ``year`` - The quota period is one year."""

    remaining: Optional[float] = UNSET
    """The number of AI credits that are remaining for the authenticated user."""

    reset_date: Optional[str] = UNSET
    """The date of the user's next AI credits reset."""

    used: Optional[float] = UNSET
    """The number of AI credits that have been spent."""


class AiCreditsQuotaDict(TypedDict):
    available: NotRequired[float]
    balances: NotRequired[list[Balance | BalanceDict]]
    period: NotRequired[PeriodOrStr]
    remaining: NotRequired[float]
    reset_date: NotRequired[str]
    used: NotRequired[float]
