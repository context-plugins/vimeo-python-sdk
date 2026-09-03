from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VideosVersionsRequest1(SdkBaseModel):
    description: Optional[str] = UNSET
    """A description of the video version. This description can make use of the full unicode character set."""

    is_current: Optional[bool] = UNSET
    """Whether the video version is active."""


class VideosVersionsRequest1Dict(TypedDict):
    description: NotRequired[str]
    is_current: NotRequired[bool]
