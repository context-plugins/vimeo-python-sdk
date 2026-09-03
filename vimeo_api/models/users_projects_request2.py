from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UsersProjectsRequest2(SdkBaseModel):
    name: str
    """The name of the folder."""


class UsersProjectsRequest2Dict(TypedDict):
    name: str
