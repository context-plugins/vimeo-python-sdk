from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .monthly import Monthly, MonthlyDict


class Subscription2(SdkBaseModel):
    monthly: Optional[Monthly] = UNSET


class Subscription2Dict(TypedDict):
    monthly: NotRequired[MonthlyDict]
