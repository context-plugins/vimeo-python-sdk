from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LiveEventsComposerScenesRequest(SdkBaseModel):
    scene_type: Optional[str] = UNSET
    """The type of scene to create. Defaults to ``live``."""


class LiveEventsComposerScenesRequestDict(TypedDict):
    scene_type: NotRequired[str]
