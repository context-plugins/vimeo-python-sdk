from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .requested_clip import RequestedClip, RequestedClipDict
from .users2 import Users2, Users2Dict
from .videos6 import Videos6, Videos6Dict


class Connections6(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    requested_clip: RequestedClip
    """Information about the requested video."""

    users: Users2
    """Information about the members or moderators of the group."""

    videos: Videos6
    """Information about the videos contained within the group."""


class Connections6Dict(TypedDict):
    requested_clip: RequestedClipDict
    users: Users2Dict
    videos: Videos6Dict
