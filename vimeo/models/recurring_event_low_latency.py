from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RecurringEventLowLatency(SdkBaseModel):
    low_latency: bool = Field(alias="lowLatency")
    """Whether the low-latency option is enabled."""


class RecurringEventLowLatencyDict(TypedDict):
    low_latency: bool
