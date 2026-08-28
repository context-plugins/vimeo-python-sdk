from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .page1 import Page1, Page1Dict


class Interactions13(SdkBaseModel):
    """An object containing information about how the authenticated user can interact with the video's On Demand
    page."""

    page: Page1
    """Information about how the authenticated user can interact with the connection to the video's On Demand page."""


class Interactions13Dict(TypedDict):
    page: Page1 | Page1Dict
