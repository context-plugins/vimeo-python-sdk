from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections21 import Connections21, Connections21Dict


class Metadata22(SdkBaseModel):
    """Metadata about the portfolio."""

    connections: Connections21
    """A list of resource URIs related to the portfolio."""


class Metadata22Dict(TypedDict):
    connections: Connections21 | Connections21Dict
