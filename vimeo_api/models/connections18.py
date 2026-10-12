from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .codes import Codes, CodesDict


class Connections18(SdkBaseModel):
    """A list of resource URIs related to the promotion."""

    codes: Codes
    """Information about the codes associated with the promotion."""


class Connections18Dict(TypedDict):
    codes: CodesDict
