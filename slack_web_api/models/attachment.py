from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Attachment(SdkBaseModel):
    fallback: Optional[str] = UNSET
    id: int
    image_bytes: Optional[int] = UNSET
    image_height: Optional[int] = UNSET
    image_url: Optional[str] = UNSET
    image_width: Optional[int] = UNSET


class AttachmentDict(TypedDict):
    fallback: NotRequired[str]
    id: int
    image_bytes: NotRequired[int]
    image_height: NotRequired[int]
    image_url: NotRequired[str]
    image_width: NotRequired[int]
