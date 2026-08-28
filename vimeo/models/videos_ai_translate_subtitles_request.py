from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosAiTranslateSubtitlesRequest(SdkBaseModel):
    language: Optional[str] = UNSET
    """The target language for translation as a language code. Use the #get_ai_languages endpoint for a list of
    supported languages."""

    texttrack_id: Optional[float] = UNSET
    """The ID of the text track to use as the translation source. When omitted, the system uses the video's primary
    transcript. Use ``GET /videos/{video_id}/texttracks`` to list available text tracks."""


class VideosAiTranslateSubtitlesRequestDict(TypedDict):
    language: NotRequired[str]
    texttrack_id: NotRequired[float]
