from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.status12 import Status12OrStr


class PreLiveVideo(SdkBaseModel):
    """Information about the event's pre-live video, where applicable. A pre-live video is either activated or in the
    process of being activated."""

    options: list[str]
    """An array of HTTP methods permitted on this URI."""

    status: Status12OrStr
    """The status of the pre-live video's RTMP link.

    Option descriptions:
     * ``pending`` - Vimeo is working on setting up the connection.
     * ``ready`` - Resources have been provisioned for the event.
     * ``streaming`` - Live video is currently streaming to the RTMP link.
     * ``unavailable`` - The connection is ready, but streaming to the RTMP link has not yet begun."""

    uri: str
    """The API URI that resolves to the connection data."""


class PreLiveVideoDict(TypedDict):
    options: list[str]
    status: Status12OrStr
    uri: str
