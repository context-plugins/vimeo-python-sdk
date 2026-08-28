from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.privacy6 import Privacy6OrStr
from .enums.service_name import ServiceNameOrStr
from .enums.state import StateOrStr
from .enums.type19 import Type19OrStr
from .metadata16 import Metadata16, Metadata16Dict


class EventDestination(SdkBaseModel):
    display_name: str
    """The name of the destination target, whether a page, profile name, or the like."""

    id: float
    """The ID of the destination."""

    is_enabled: bool
    """Whether the destination is enabled."""

    live_clip_id: float
    """The ID of the live video."""

    metadata: Metadata16
    """Metadata about the event destination."""

    privacy: Privacy6OrStr | None
    """The privacy setting of the destination.

    Option descriptions:
     * ``CONNECTIONS`` - The privacy setting is ``CONNECTIONS`` for LinkedIn.
     * ``PUBLIC`` - The privacy setting is ``PUBLIC`` for LinkedIn.
     * ``all_friends`` - The privacy setting is ``all_friends`` for Facebook.
     * ``everyone`` - The privacy setting is ``everyone`` for Facebook.
     * ``private`` - The privacy setting is ``private`` for YouTube.
     * ``public`` - The privacy setting is ``public`` for YouTube.
     * ``self`` - The privacy setting is ``self`` for Facebook.
     * ``unlisted`` - The privacy setting is ``unlisted`` for YouTube."""

    provider_broadcast_id: str | None
    """The broadcast ID of the destination service."""

    provider_destination_id: str | None
    """The destination ID of the destination service."""

    provider_user_id: str | None
    """The user ID of the destination service."""

    provider_video_id: str | None
    """The ID of the scheduled live video."""

    scheduled_at: float | None
    """The time in Unix timestamp format when live streaming is scheduled to start."""

    service_name: ServiceNameOrStr
    """The name of the destination service.

    Option descriptions:
     * ``custom_rtmp`` - The destination service is custom RTMP.
     * ``facebook`` - The destination service is Facebook Live.
     * ``linkedin`` - The destination service is LinkedIn Live.
     * ``youtube`` - The destination service is YouTube Live."""

    state: StateOrStr
    """The status of the destination.

    Option descriptions:
     * ``0`` - The status is OK.
     * ``1`` - An error occurred. Check the ``state_message`` field for details."""

    state_message: str | None
    """The message that describes the state of the destination."""

    stream_key: str | None
    """The stream key for the simulcast destination."""

    stream_url: str | None
    """The RTMP URL to stream to."""

    type_: Type19OrStr = Field(alias="type")
    """The type of the simulcast destination.

    Option descriptions:
     * ``channel`` - The destination is a YouTube channel.
     * ``custom`` - The destination is custom.
     * ``organization`` - The destination is a LinkedIn organization.
     * ``page`` - The destination is a Facebook page.
     * ``profile`` - The destination is a Facebook or LinkedIn profile."""

    user_display_name: str
    """The name of the destination's owner."""

    user_id: float
    """The ID of the destination's owner."""


class EventDestinationDict(TypedDict):
    display_name: str
    id: float
    is_enabled: bool
    live_clip_id: float
    metadata: Metadata16 | Metadata16Dict
    privacy: Privacy6OrStr | None
    provider_broadcast_id: str | None
    provider_destination_id: str | None
    provider_user_id: str | None
    provider_video_id: str | None
    scheduled_at: float | None
    service_name: ServiceNameOrStr
    state: StateOrStr
    state_message: str | None
    stream_key: str | None
    stream_url: str | None
    type_: Type19OrStr
    user_display_name: str
    user_id: float
