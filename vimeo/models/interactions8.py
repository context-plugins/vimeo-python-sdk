from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Interactions8(SdkBaseModel):
    """An object containing the actions that the user can perform on the comment."""

    report: Any
    """Metadata for reporting the comment as inappropriate or violating community guidelines."""


class Interactions8Dict(TypedDict):
    report: Any
