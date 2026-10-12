from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections7 import Connections7, Connections7Dict


class Metadata7(SdkBaseModel):
    """Information about the activity's metadata."""

    connections: Connections7
    """A list of resource URIs related to the activity."""


class Metadata7Dict(TypedDict):
    connections: Connections7Dict
