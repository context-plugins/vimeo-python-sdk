from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections1 import Connections1, Connections1Dict
from .interactions1 import Interactions1, Interactions1Dict


class Metadata1(SdkBaseModel):
    """Metadata about the channel."""

    connections: Connections1
    """A collection of information that is connected to this resource."""

    interactions: Interactions1 | None
    """A list of resource URIs related to the channel."""


class Metadata1Dict(TypedDict):
    connections: Connections1Dict
    interactions: Interactions1Dict | None
