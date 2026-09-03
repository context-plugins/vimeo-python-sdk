from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections3 import Connections3, Connections3Dict
from .interactions2 import Interactions2, Interactions2Dict
from .public_videos import PublicVideos, PublicVideosDict


class Metadata3(SdkBaseModel):
    """The authenticated user's metadata."""

    connections: Connections3
    """The list of resource URIs related to the authenticated user."""

    interactions: Interactions2
    ms_teams_encrypted_team_id: str | None
    """Information about the Microsoft Teams encrypted team ID."""

    public_videos: PublicVideos


class Metadata3Dict(TypedDict):
    connections: Connections3 | Connections3Dict
    interactions: Interactions2 | Interactions2Dict
    ms_teams_encrypted_team_id: str | None
    public_videos: PublicVideos | PublicVideosDict
