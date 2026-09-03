from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsCategoriesRequest(SdkBaseModel):
    channels: list[str]
    """The array of category URIs to add."""


class ChannelsCategoriesRequestDict(TypedDict):
    channels: list[str]
