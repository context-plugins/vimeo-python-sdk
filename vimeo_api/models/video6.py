from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Video6(SdkBaseModel):
    uri: Optional[str] = UNSET
    """The URI of a video to add."""


class Video6Dict(TypedDict):
    uri: NotRequired[str]
