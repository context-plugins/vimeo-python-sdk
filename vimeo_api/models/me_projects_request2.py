from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeProjectsRequest2(SdkBaseModel):
    name: str
    """The name of the folder."""


class MeProjectsRequest2Dict(TypedDict):
    name: str
