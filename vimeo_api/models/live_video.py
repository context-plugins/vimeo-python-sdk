from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class LiveVideo(SdkBaseModel):
    """Information about the event's live video, where applicable."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    status: Literal["streaming"] = "streaming"
    """The status of the live video's RTMP link.

    Option descriptions:
     * ``streaming`` - The stream is open and receiving content."""

    uri: str
    """The API URI that resolves to the connection data."""


class LiveVideoDict(TypedDict):
    options: list[str]
    status: NotRequired[Literal["streaming"]]
    uri: str
