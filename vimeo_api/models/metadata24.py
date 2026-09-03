from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections23 import Connections23, Connections23Dict


class Metadata24(SdkBaseModel):
    """The item's metadata."""

    connections: Connections23
    """A list of resource URIs related to the item."""


class Metadata24Dict(TypedDict):
    connections: Connections23 | Connections23Dict
