from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersProjectsVideosRequest1(SdkBaseModel):
    uris: str
    """A comma-separated list of video URIs to add."""


class UsersProjectsVideosRequest1Dict(TypedDict):
    uris: str
