from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EnableDownload(SdkBaseModel):
    """Information about enabling the download functionality during playback."""

    is_upgrade: bool
    """Whether an upgrade is required to enable the download functionality during playback."""

    value: bool
    """Whether to enable the download functionality during playback."""


class EnableDownloadDict(TypedDict):
    is_upgrade: bool
    value: bool
