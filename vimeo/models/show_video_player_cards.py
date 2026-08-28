from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowVideoPlayerCards(SdkBaseModel):
    """Information about showing video player cards on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show video player cards on the showcase page."""

    value: bool
    """Whether to show video player cards on the showcase page."""


class ShowVideoPlayerCardsDict(TypedDict):
    is_upgrade: bool
    value: bool
