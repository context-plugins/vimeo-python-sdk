from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ObjsIcon(SdkBaseModel):
    image_102: Optional[str] = UNSET
    image_132: Optional[str] = UNSET
    image_230: Optional[str] = UNSET
    image_34: Optional[str] = UNSET
    image_44: Optional[str] = UNSET
    image_68: Optional[str] = UNSET
    image_88: Optional[str] = UNSET
    image_default: Optional[bool] = UNSET


class ObjsIconDict(TypedDict):
    image_102: NotRequired[str]
    image_132: NotRequired[str]
    image_230: NotRequired[str]
    image_34: NotRequired[str]
    image_44: NotRequired[str]
    image_68: NotRequired[str]
    image_88: NotRequired[str]
    image_default: NotRequired[bool]
