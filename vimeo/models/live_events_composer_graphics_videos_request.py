from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LiveEventsComposerGraphicsVideosRequest(SdkBaseModel):
    video_id: float
    """The ID of the associated video."""


class LiveEventsComposerGraphicsVideosRequestDict(TypedDict):
    video_id: float
