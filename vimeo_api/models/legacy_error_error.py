from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LegacyErrorError(SdkBaseModel):
    error: str
    """The error message."""


class LegacyErrorErrorDict(TypedDict):
    error: str
