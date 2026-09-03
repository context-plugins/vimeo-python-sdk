from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections18 import Connections18, Connections18Dict


class Metadata19(SdkBaseModel):
    """The video's metadata."""

    connections: Connections18
    """A list of resource URIs related to the promotion."""


class Metadata19Dict(TypedDict):
    connections: Connections18 | Connections18Dict
