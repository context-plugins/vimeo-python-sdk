from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ViewTeamMembers(SdkBaseModel):
    """Information about whether a user can view the team members associated with a video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class ViewTeamMembersDict(TypedDict):
    options: list[str]
    uri: str
