from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PublicVideos(SdkBaseModel):
    total: float
    """The total number of public videos that the authenticated user has uploaded."""


class PublicVideosDict(TypedDict):
    total: float
