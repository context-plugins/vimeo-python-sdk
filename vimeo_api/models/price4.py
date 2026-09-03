from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Price4(SdkBaseModel):
    usd: Optional[float] = Field(default=UNSET, alias="USD")
    """The rental price per episode in United States dollars. This parameter is applicable only when **type** is
    ``series``, and it's required when **episode.rent.active** is ``true``."""


class Price4Dict(TypedDict):
    usd: NotRequired[float]
