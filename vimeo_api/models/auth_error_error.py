from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AuthErrorError(SdkBaseModel):
    error: str
    """The name of the error."""

    error_description: str
    """The description of the error."""


class AuthErrorErrorDict(TypedDict):
    error: str
    error_description: str
