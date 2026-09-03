from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Add(SdkBaseModel):
    uri: Optional[str] = UNSET
    """The showcase URI to add the video to."""


class AddDict(TypedDict):
    uri: NotRequired[str]
