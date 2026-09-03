from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ShowVideoDetails(SdkBaseModel):
    """Information about showing video details on the showcase page."""

    is_upgrade: bool
    """Whether an upgrade is required to show video details on the showcase page."""

    value: bool
    """Whether to show video details on the showcase page."""


class ShowVideoDetailsDict(TypedDict):
    is_upgrade: bool
    value: bool
