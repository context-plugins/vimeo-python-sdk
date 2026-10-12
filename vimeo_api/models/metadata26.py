from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .connections24 import Connections24, Connections24Dict


class Metadata26(SdkBaseModel):
    """The metadata of the team membership."""

    connections: Connections24
    """A list of resource URIs related to the user."""


class Metadata26Dict(TypedDict):
    connections: Connections24Dict
