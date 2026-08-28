from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AiContent(SdkBaseModel):
    """Information about the video's AI content."""

    audio: Optional[bool] = UNSET
    """Whether the video contains AI-generated audio."""

    audio_auto: Optional[bool] = UNSET
    """Whether the video contains AI-generated audio that is marked automatically."""

    visual: Optional[bool] = UNSET
    """Whether the video contains AI-generated visuals."""

    visual_auto: Optional[bool] = UNSET
    """Whether the video contains AI-generated visuals that are marked automatically."""


class AiContentDict(TypedDict):
    audio: NotRequired[bool]
    audio_auto: NotRequired[bool]
    visual: NotRequired[bool]
    visual_auto: NotRequired[bool]
