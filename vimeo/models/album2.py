from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Album2(SdkBaseModel):
    """Information about the associated showcase."""

    embed_code: str
    """The responsive embed code for the associated showcase."""

    id: float
    """The ID of the associated showcase."""

    privacy: str
    """The privacy setting of the associated showcase."""

    title: str
    """The title of the associated showcase."""


class Album2Dict(TypedDict):
    embed_code: str
    id: float
    privacy: str
    title: str
