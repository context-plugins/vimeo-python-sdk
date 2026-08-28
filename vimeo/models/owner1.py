from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Owner1(SdkBaseModel):
    """Information about the team owner."""

    display_name: str
    """The display name of the team owner."""

    email: str
    """The team owner's email address."""

    invites_remaining: float
    """The total number of remaining team member invites."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    total: float
    """The total number of owners on this connection."""

    total_members: float
    """The total number of team members for the specified team owner."""

    uri: str
    """The API URI that resolves to the connection data."""


class Owner1Dict(TypedDict):
    display_name: str
    email: str
    invites_remaining: float
    options: list[str]
    total: float
    total_members: float
    uri: str
