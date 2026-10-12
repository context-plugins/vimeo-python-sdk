from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .add_moderators import AddModerators, AddModeratorsDict
from .add_to import AddTo, AddToDict
from .follow1 import Follow1, Follow1Dict
from .moderate_videos import ModerateVideos, ModerateVideosDict


class Interactions1(SdkBaseModel):
    """A list of resource URIs related to the channel."""

    add_moderators: AddModerators
    """An action indicating that the authenticated user is the owner of the channel and may therefore add other users as
    channel moderators. This data requires a bearer token with the ``private`` scope."""

    add_to: AddTo | None
    """When a channel appears in the context of adding or removing a video from it
    (``/videos/{video_id}/available_channels``), include information about adding or removing the video. This data
    requires a bearer token with the ``private`` scope."""

    follow: Follow1
    """An action indicating if the authenticated user has followed this channel. This data requires a bearer token with
    the ``private`` scope."""

    moderate_videos: ModerateVideos
    """An action indicating that the authenticated user is a moderator of the channel and may therefore add or remove
    videos from the channel. This data requires a bearer token with the ``private`` scope."""


class Interactions1Dict(TypedDict):
    add_moderators: AddModeratorsDict
    add_to: AddToDict | None
    follow: Follow1Dict
    moderate_videos: ModerateVideosDict
