from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosAiTranscribeRequest(SdkBaseModel):
    language: Optional[str] = UNSET
    """The language for transcription as a BCP 47 language code. When omitted, the system auto-detects the spoken
    language from the video's audio. Use the #get_ai_languages endpoint for a list of supported languages."""


class VideosAiTranscribeRequestDict(TypedDict):
    language: NotRequired[str]
