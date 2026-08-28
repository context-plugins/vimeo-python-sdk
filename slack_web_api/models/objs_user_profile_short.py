from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ObjsUserProfileShort(SdkBaseModel):
    avatar_hash: str
    display_name: str
    display_name_normalized: Optional[str] = UNSET
    first_name: str | None
    image_72: str
    is_restricted: bool
    is_ultra_restricted: bool
    name: str
    real_name: str
    real_name_normalized: Optional[str] = UNSET
    team: str


class ObjsUserProfileShortDict(TypedDict):
    avatar_hash: str
    display_name: str
    display_name_normalized: NotRequired[str]
    first_name: str | None
    image_72: str
    is_restricted: bool
    is_ultra_restricted: bool
    name: str
    real_name: str
    real_name_normalized: NotRequired[str]
    team: str
