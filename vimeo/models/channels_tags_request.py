from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ChannelsTagsRequest(SdkBaseModel):
    name: str
    """The name of the tag to assign."""


class ChannelsTagsRequestDict(TypedDict):
    name: str
