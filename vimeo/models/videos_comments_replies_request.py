from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosCommentsRepliesRequest(SdkBaseModel):
    richtext: Optional[str] = UNSET
    """The rich comment in JSON stringified form."""

    text: str
    """The reply to the comment."""


class VideosCommentsRepliesRequestDict(TypedDict):
    richtext: NotRequired[str]
    text: str
