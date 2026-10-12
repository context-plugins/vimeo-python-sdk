from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections11 import Connections11, Connections11Dict
from .interactions7 import Interactions7, Interactions7Dict


class Metadata11(SdkBaseModel):
    """Metadata about the showcase."""

    connections: Connections11
    """Information about showcase connections."""

    interactions: Interactions7 | None
    """A list of resource URIs related to the showcase."""


class Metadata11Dict(TypedDict):
    connections: Connections11Dict
    interactions: Interactions7Dict | None
