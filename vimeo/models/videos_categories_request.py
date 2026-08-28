from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class VideosCategoriesRequest(SdkBaseModel):
    category: list[str]
    """An array of the names of the desired categories."""


class VideosCategoriesRequestDict(TypedDict):
    category: list[str]
