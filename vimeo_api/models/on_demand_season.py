from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata20 import Metadata20, Metadata20Dict
from .user import User, UserDict


class OnDemandSeason(SdkBaseModel):
    description: str
    """The description of the season."""

    metadata: Metadata20
    name: str
    """The name of the season."""

    position: float
    """The position of the season relative to other seasons in the series."""

    resource_key: str
    """The unique identifier of the On Demand season."""

    type_: str = Field(alias="type")
    """The type of the season."""

    uri: str
    """The season container's relative URI."""

    user: User | None
    """The creator of the season's On Demand page."""


class OnDemandSeasonDict(TypedDict):
    description: str
    metadata: Metadata20Dict
    name: str
    position: float
    resource_key: str
    type_: str
    uri: str
    user: UserDict | None
