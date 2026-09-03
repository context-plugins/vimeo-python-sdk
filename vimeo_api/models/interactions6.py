from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .page import Page, PageDict


class Interactions6(SdkBaseModel):
    page: Page
    """Interactions for On Demand pages that belong to the genre."""


class Interactions6Dict(TypedDict):
    page: Page | PageDict
