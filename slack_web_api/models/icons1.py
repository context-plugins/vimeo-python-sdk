from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Icons1(SdkBaseModel):
    emoji: Optional[str] = UNSET
    image_64: Optional[str] = UNSET


class Icons1Dict(TypedDict):
    emoji: NotRequired[str]
    image_64: NotRequired[str]
