from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorError(SdkBaseModel):
    developer_message: str
    """The error message that technical users receive."""

    error: str
    """The error message that general users receive."""

    error_code: float
    """The error code."""

    link: str
    """A link to more information about the error."""


class ErrorErrorDict(TypedDict):
    developer_message: str
    error: str
    error_code: float
    link: str
