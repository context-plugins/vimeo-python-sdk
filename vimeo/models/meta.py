from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Meta(SdkBaseModel):
    """The additional information about the scene."""

    is_scheduled: bool
    """If the scene is scheduled to play automatically when stream starts."""


class MetaDict(TypedDict):
    is_scheduled: bool
