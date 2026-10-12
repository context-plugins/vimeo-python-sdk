from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .pages import Pages, PagesDict


class Connections8(SdkBaseModel):
    """A collection of information connected to this resource."""

    pages: Pages
    """Information about the On Demand pages related to this group."""


class Connections8Dict(TypedDict):
    pages: PagesDict
