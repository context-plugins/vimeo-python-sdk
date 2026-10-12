from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .upload4 import Upload4, Upload4Dict


class VideosVersionsRequest(SdkBaseModel):
    file_name: str
    """The name of the version."""

    upload: Upload4


class VideosVersionsRequestDict(TypedDict):
    file_name: str
    upload: Upload4Dict
