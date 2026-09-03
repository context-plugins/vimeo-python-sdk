from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections20 import Connections20, Connections20Dict
from .interactions14 import Interactions14, Interactions14Dict


class Metadata21(SdkBaseModel):
    """Metadata information about the video."""

    connections: Connections20
    interactions: Interactions14


class Metadata21Dict(TypedDict):
    connections: Connections20 | Connections20Dict
    interactions: Interactions14 | Interactions14Dict
