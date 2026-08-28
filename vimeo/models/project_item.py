from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .album import Album, AlbumDict
from .enums.type21 import Type21OrStr
from .metadata24 import Metadata24, Metadata24Dict
from .project import Project, ProjectDict
from .recurring_event import RecurringEvent, RecurringEventDict
from .video import Video, VideoDict


class ProjectItem(SdkBaseModel):
    folder: Optional[Project] = UNSET
    """The project item folder."""

    live_event: Optional[RecurringEvent] = UNSET
    """The project item event."""

    metadata: Metadata24
    """The item's metadata."""

    shared_date: Optional[str] = UNSET
    """The time in ISO 8601 format when the item was shared."""

    showcase: Optional[Album] = UNSET
    """The project item showcase."""

    type_: Type21OrStr = Field(alias="type")
    """The project item type.

    Option descriptions:
     * ``folder`` - The project item is a folder.
     * ``live_event`` - The project item is an event.
     * ``showcase`` - The project item is a showcase.
     * ``video`` - The project item is a video."""

    video: Optional[Video] = UNSET
    """The project item video."""


class ProjectItemDict(TypedDict):
    folder: NotRequired[Project | ProjectDict]
    live_event: NotRequired[RecurringEvent | RecurringEventDict]
    metadata: Metadata24 | Metadata24Dict
    shared_date: NotRequired[str]
    showcase: NotRequired[Album | AlbumDict]
    type_: Type21OrStr
    video: NotRequired[Video | VideoDict]
