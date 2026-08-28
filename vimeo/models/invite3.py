from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Invite3(SdkBaseModel):
    """Information about where and how to invite a team member to a showcase."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    uri: str
    """The API URI that resolves to the connection data."""


class Invite3Dict(TypedDict):
    options: list[str]
    uri: str
