from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections import Connections, ConnectionsDict
from .interactions import Interactions, InteractionsDict


class Metadata(SdkBaseModel):
    """Metadata about the category."""

    connections: Connections
    """A collection of information that is connected to this resource."""

    interactions: Interactions
    """The permissible actions related to the category."""


class MetadataDict(TypedDict):
    connections: Connections | ConnectionsDict
    interactions: Interactions | InteractionsDict
