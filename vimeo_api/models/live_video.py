from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status11 import Status11OrStr


class LiveVideo(SdkBaseModel):
    """Information about the event's live video, where applicable."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    status: Status11OrStr
    """The status of the live video's RTMP link.

    Option descriptions:
     * ``streaming`` - The stream is open and receiving content."""

    uri: str
    """The API URI that resolves to the connection data."""


class LiveVideoDict(TypedDict):
    options: list[str]
    status: Status11OrStr
    uri: str
