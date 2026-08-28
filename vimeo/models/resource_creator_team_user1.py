from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResourceCreatorTeamUser1(SdkBaseModel):
    """Information about the team user who created the folder. This data requires a bearer token with the ``private``
    scope."""

    uri: str
    """The URI for the team user who created the folder. This data requires a bearer token with the ``private``
    scope."""


class ResourceCreatorTeamUser1Dict(TypedDict):
    uri: str
