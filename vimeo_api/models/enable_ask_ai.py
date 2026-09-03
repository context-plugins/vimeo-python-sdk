from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableAskAi(SdkBaseModel):
    """Information about enabling the Ask AI functionality during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to enable the Ask AI functionality during playback."""

    value: bool
    """Whether to enable the Ask AI functionality during playback."""


class EnableAskAiDict(TypedDict):
    is_upgrade: bool
    value: bool
