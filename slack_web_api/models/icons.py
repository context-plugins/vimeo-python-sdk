from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Icons(SdkBaseModel):
    image_36: str
    image_48: str
    image_72: str


class IconsDict(TypedDict):
    image_36: str
    image_48: str
    image_72: str
