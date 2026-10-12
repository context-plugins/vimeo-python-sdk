from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections5 import Connections5, Connections5Dict
from .interactions4 import Interactions4, Interactions4Dict


class Metadata5(SdkBaseModel):
    """Information about the folders's metadata."""

    connections: Connections5
    """A list of resource URIs related to the folder."""

    interactions: Interactions4
    """A list of permitted interactions related to the folder."""


class Metadata5Dict(TypedDict):
    connections: Connections5Dict
    interactions: Interactions4Dict
