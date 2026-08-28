from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price3(SdkBaseModel):
    usd: Optional[float] = Field(default=UNSET, alias="USD")
    """The purchase price per episode in United States dollars. This parameter is required when **episodes.buy.active**
    is ``true``."""


class Price3Dict(TypedDict):
    usd: NotRequired[float]
