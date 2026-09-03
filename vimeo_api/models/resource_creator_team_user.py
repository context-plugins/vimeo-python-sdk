from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResourceCreatorTeamUser(SdkBaseModel):
    """Information about the team user who uploaded the video. This data requires a bearer token with the ``private``
    scope."""

    uri: str
    """The URI for the team user who uploaded the video. This data requires a bearer token with the ``private``
    scope."""


class ResourceCreatorTeamUserDict(TypedDict):
    uri: str
