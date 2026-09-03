from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .archive import Archive, ArchiveDict
from .enums.status13 import Status13OrStr
from .enums.stream_mode import StreamModeOrStr
from .ingest import Ingest, IngestDict
from .metering import Metering, MeteringDict


class EventSessionStatus(SdkBaseModel):
    archive: Archive
    """Information about the archive data."""

    can_manage: bool
    """Whether the current user can manage the event."""

    id: float
    """The ID of the live video."""

    ingest: Ingest
    """The ingest of the video."""

    metering: Metering
    """The metering status of the live video."""

    status: Status13OrStr | None
    """The status of the event.

    Option descriptions:
     * ``ended`` - The event has ended.
     * ``started`` - The event has started."""

    stream_mode: StreamModeOrStr
    """The stream mode of the event.

    Option descriptions:
     * ``live`` - The stream is live playback.
     * ``record`` - The stream is in record mode.
     * ``simulive`` - The stream is scheduled media playback."""


class EventSessionStatusDict(TypedDict):
    archive: Archive | ArchiveDict
    can_manage: bool
    id: float
    ingest: Ingest | IngestDict
    metering: Metering | MeteringDict
    status: Status13OrStr | None
    stream_mode: StreamModeOrStr
