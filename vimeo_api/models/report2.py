from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Report2(SdkBaseModel):
    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    reason: list[str]
    """A list of predefined reasons for which the comment can be reported. These reasons correspond to the available
    flagging options."""

    uri: str
    """The URI to use for sending a report request for the comment."""


class Report2Dict(TypedDict):
    options: list[str]
    reason: list[str]
    uri: str
