from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ResponseMetadata(SdkBaseModel):
    next_cursor: str


class ResponseMetadataDict(TypedDict):
    next_cursor: str
