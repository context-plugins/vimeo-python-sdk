from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .channels import Channels, ChannelsDict
from .groups import Groups, GroupsDict
from .users import Users, UsersDict
from .videos import Videos, VideosDict


class Connections(SdkBaseModel):
    """A collection of information that is connected to this resource."""

    channels: Channels
    """Information about the channels related to this category."""

    groups: Groups
    """Information about the groups related to this category."""

    users: Users
    """Information about the users related to this category."""

    videos: Videos
    """Information about the videos related to this category."""


class ConnectionsDict(TypedDict):
    channels: Channels | ChannelsDict
    groups: Groups | GroupsDict
    users: Users | UsersDict
    videos: Videos | VideosDict
