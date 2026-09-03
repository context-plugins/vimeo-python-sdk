from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LegacyError(SdkBaseModel):
    error: str
    """The error message."""


class LegacyErrorDict(TypedDict):
    error: str
