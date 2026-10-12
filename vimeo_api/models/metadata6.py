from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections6 import Connections6, Connections6Dict
from .interactions5 import Interactions5, Interactions5Dict


class Metadata6(SdkBaseModel):
    """Metadata about the group."""

    connections: Connections6
    """A collection of information that is connected to this resource."""

    interactions: Interactions5
    """User actions that have involved the group. This data requires a bearer token with the ``private`` scope."""


class Metadata6Dict(TypedDict):
    connections: Connections6Dict
    interactions: Interactions5Dict
