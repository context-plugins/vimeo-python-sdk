from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections22 import Connections22, Connections22Dict


class Metadata23(SdkBaseModel):
    """Metadata about the preset."""

    connections: Connections22
    """A list of resource URIs related to the preset."""


class Metadata23Dict(TypedDict):
    connections: Connections22 | Connections22Dict
