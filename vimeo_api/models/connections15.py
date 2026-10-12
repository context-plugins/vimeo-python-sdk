from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .live_video import LiveVideo, LiveVideoDict
from .pictures3 import Pictures3, Pictures3Dict
from .pre_live_video import PreLiveVideo, PreLiveVideoDict
from .team_member import TeamMember, TeamMemberDict
from .videos10 import Videos10, Videos10Dict


class Connections15(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    live_video: LiveVideo | None
    """Information about the event's live video, where applicable."""

    pictures: Pictures3
    """Information about the event's thumbnails."""

    pre_live_video: PreLiveVideo | None
    """Information about the event's pre-live video, where applicable. A pre-live video is either activated or in the
    process of being activated."""

    team_member: TeamMember | None
    """Information about the team member who owns the event."""

    videos: Videos10
    """Information about the videos that belong to the event."""


class Connections15Dict(TypedDict):
    live_video: LiveVideoDict | None
    pictures: Pictures3Dict
    pre_live_video: PreLiveVideoDict | None
    team_member: TeamMemberDict | None
    videos: Videos10Dict
