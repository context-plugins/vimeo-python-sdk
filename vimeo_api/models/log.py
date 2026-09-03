from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Log(SdkBaseModel):
    play: Optional[str] = UNSET
    """The URL to record a Play logging event."""


class LogDict(TypedDict):
    play: NotRequired[str]
