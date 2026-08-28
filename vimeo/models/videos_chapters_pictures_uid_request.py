from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosChaptersPicturesUidRequest(SdkBaseModel):
    active: Optional[bool] = UNSET
    """Whether to set the chapter thumbnail as active."""


class VideosChaptersPicturesUidRequestDict(TypedDict):
    active: NotRequired[bool]
