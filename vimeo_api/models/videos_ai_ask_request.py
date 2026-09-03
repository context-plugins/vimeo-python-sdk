from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosAiAskRequest(SdkBaseModel):
    question: Optional[str] = UNSET
    """The question to ask about the video content. Maximum 500 characters."""


class VideosAiAskRequestDict(TypedDict):
    question: NotRequired[str]
