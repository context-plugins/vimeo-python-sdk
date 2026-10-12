from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .child_text_tracks import ChildTextTracks, ChildTextTracksDict
from .parent_text_track import ParentTextTrack, ParentTextTrackDict


class Connections25(SdkBaseModel):
    child_text_tracks: Optional[ChildTextTracks] = UNSET
    """Metadata for the child text tracks. This data requires a bearer token with the ``private`` scope."""

    parent_text_track: Optional[ParentTextTrack] = UNSET
    """Metadata for the parent text track."""


class Connections25Dict(TypedDict):
    child_text_tracks: NotRequired[ChildTextTracksDict]
    parent_text_track: NotRequired[ParentTextTrackDict]
