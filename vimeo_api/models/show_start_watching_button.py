from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowStartWatchingButton(SdkBaseModel):
    """Information about showing the button to start watching."""

    is_upgrade: bool
    """Whether an upgrade is required for showing the button to start watching."""

    value: bool
    """Whether to show the button to start watching."""


class ShowStartWatchingButtonDict(TypedDict):
    is_upgrade: bool
    value: bool
