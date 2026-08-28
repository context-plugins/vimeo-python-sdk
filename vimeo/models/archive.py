from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Archive(SdkBaseModel):
    """Information about the archive data."""

    clip_id: float
    """The ID of the archived video."""

    status: float | None
    """The status of the archive data."""


class ArchiveDict(TypedDict):
    clip_id: float
    status: float | None
