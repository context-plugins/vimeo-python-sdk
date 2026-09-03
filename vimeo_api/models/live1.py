from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Live1(SdkBaseModel):
    """The associated live stream object. This data requires a bearer token with the ``private`` scope."""

    stream_end_time: str | None
    """The time in ISO 8601 format when the live stream ended. This data requires a bearer token with the ``private``
    scope."""

    stream_start_time: str | None
    """The time in ISO 8601 format when the live stream started. This data requires a bearer token with the ``private``
    scope."""


class Live1Dict(TypedDict):
    stream_end_time: str | None
    stream_start_time: str | None
