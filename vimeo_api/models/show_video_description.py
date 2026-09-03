from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowVideoDescription(SdkBaseModel):
    """Information about showing the description on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show the description on the showcase page."""

    value: bool
    """Whether to show the description on the showcase page."""


class ShowVideoDescriptionDict(TypedDict):
    is_upgrade: bool
    value: bool
