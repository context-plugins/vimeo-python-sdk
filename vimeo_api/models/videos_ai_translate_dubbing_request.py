from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosAiTranslateDubbingRequest(SdkBaseModel):
    accent: Optional[str] = UNSET
    """The accent for the dubbed audio. Each language has its own set of available accents — use the #get_ai_languages
    endpoint to list them. Common values include ``auto`` (AI-selected voice) and ``original`` (clones the speaker's
    voice, requires account capability). When omitted for regional variants (e.g. ``es-MX``), the default accent for
    that variant is used. When omitted for base languages (e.g. ``es``), the service selects automatically."""

    language: Optional[str] = UNSET
    """The target language for dubbing as a language code. Use the #get_ai_languages endpoint for a list of supported
    languages."""


class VideosAiTranslateDubbingRequestDict(TypedDict):
    accent: NotRequired[str]
    language: NotRequired[str]
