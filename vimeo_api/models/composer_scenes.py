from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .graphic import Graphic, GraphicDict
from .meta import Meta, MetaDict


class ComposerScenes(SdkBaseModel):
    graphics: list[Graphic]
    """The collection of graphic items, such as lower thirds, polls, and images, associated with this scene."""

    id: str
    """The unique identifier of the scene."""

    meta: Meta
    """The additional information about the scene."""

    name: str
    """The name of the scene."""


class ComposerScenesDict(TypedDict):
    graphics: list[GraphicDict]
    id: str
    meta: MetaDict
    name: str
