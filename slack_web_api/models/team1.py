from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Team1(SdkBaseModel):
    domain: str
    id: str
    name: str


class Team1Dict(TypedDict):
    domain: str
    id: str
    name: str
