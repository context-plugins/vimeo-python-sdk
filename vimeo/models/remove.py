from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Remove(SdkBaseModel):
    uri: Optional[str] = UNSET
    """The showcase URI to remove the video from."""


class RemoveDict(TypedDict):
    uri: NotRequired[str]
