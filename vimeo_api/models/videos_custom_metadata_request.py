from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .field1 import Field1, Field1Dict


class VideosCustomMetadataRequest(SdkBaseModel):
    fields: Optional[list[Field1]] = UNSET
    """The custom metadata values to apply to the video."""


class VideosCustomMetadataRequestDict(TypedDict):
    fields: NotRequired[list[Field1 | Field1Dict]]
