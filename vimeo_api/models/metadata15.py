from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections15 import Connections15, Connections15Dict
from .interactions10 import Interactions10, Interactions10Dict


class Metadata15(SdkBaseModel):
    """Metadata about the event."""

    connections: Connections15
    """A collection of information that is connected to this resource."""

    interactions: Interactions10
    """A list of resource URIs related to the event."""


class Metadata15Dict(TypedDict):
    connections: Connections15Dict
    interactions: Interactions10Dict
