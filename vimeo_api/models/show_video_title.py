from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowVideoTitle(SdkBaseModel):
    """Information about showing the title on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show the title on the showcase page."""

    value: bool
    """Whether to show the title on the showcase page."""


class ShowVideoTitleDict(TypedDict):
    is_upgrade: bool
    value: bool
