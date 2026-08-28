from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .interactions11 import Interactions11, Interactions11Dict


class Metadata16(SdkBaseModel):
    """Metadata about the event destination."""

    connection_status: Any
    """Information about the connection status of the destination's user."""

    interactions: Interactions11
    """A list of resource URIs related to the event destination."""


class Metadata16Dict(TypedDict):
    connection_status: Any
    interactions: Interactions11 | Interactions11Dict
