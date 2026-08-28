from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TeamMember(SdkBaseModel):
    """Information about the team member who owns the event."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class TeamMemberDict(TypedDict):
    options: list[str]
    uri: str
