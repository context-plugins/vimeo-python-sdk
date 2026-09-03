from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Invite(SdkBaseModel):
    """Information about where and how to get a list of team members or groups who were explicitly invited to a video,
    and where and how to invite a team member to a video."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class InviteDict(TypedDict):
    options: list[str]
    uri: str
