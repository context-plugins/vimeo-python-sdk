from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeProjectsVideosRequest1(SdkBaseModel):
    uris: str
    """A comma-separated list of video URIs to add."""


class MeProjectsVideosRequest1Dict(TypedDict):
    uris: str
