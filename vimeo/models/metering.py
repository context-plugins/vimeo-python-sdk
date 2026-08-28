from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Metering(SdkBaseModel):
    """The metering status of the live video."""

    seconds_max: float
    """The maximum number of seconds."""

    seconds_remaining: float
    """The number of seconds remaining."""


class MeteringDict(TypedDict):
    seconds_max: float
    seconds_remaining: float
