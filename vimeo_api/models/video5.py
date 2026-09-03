from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Video5(SdkBaseModel):
    uri: Optional[str] = UNSET
    """The URI of a video to remove."""


class Video5Dict(TypedDict):
    uri: NotRequired[str]
