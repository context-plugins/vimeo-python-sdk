from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.period1 import Period1OrStr


class Bandwidth(SdkBaseModel):
    period: Optional[Period1OrStr] = UNSET
    """The quota period for which the bandwidth is evaluated.

    Option descriptions:
     * ``calendar_month`` - The quota period is one month.
     * ``year`` - The quota period is one year."""


class BandwidthDict(TypedDict):
    period: NotRequired[Period1OrStr]
