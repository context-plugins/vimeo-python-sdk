from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price6(SdkBaseModel):
    usd: Optional[float] = Field(default=UNSET, alias="USD")
    """The monthly subscription price in United States dollars. This parameter is required when **rent.active** and
    **buy.active** are ``false``."""


class Price6Dict(TypedDict):
    usd: NotRequired[float]
