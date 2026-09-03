from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.privacy9 import Privacy9OrStr
from .enums.service_name1 import ServiceName1OrStr
from .enums.type15 import Type15OrStr


class UsersLiveEventsDestinationsRequest(SdkBaseModel):
    display_name: str
    """The title to display for the simulcast."""

    is_enabled: Optional[bool] = UNSET
    """Whether the destination is enabled for simulcasting."""

    privacy: Optional[Privacy9OrStr] = UNSET
    """The privacy setting of the destination. Be sure to choose a value that corresponds to your service.

    Option descriptions:
     * ``CONNECTIONS`` - The privacy setting is ``CONNECTIONS`` for LinkedIn.
     * ``PUBLIC`` - The privacy setting is ``PUBLIC`` for LinkedIn.
     * ``all_friends`` - The privacy setting is ``all_friends`` for Facebook.
     * ``everyone`` - The privacy setting is ``everyone`` for Facebook.
     * ``private`` - The privacy setting is ``private`` for YouTube.
     * ``public`` - The privacy setting is ``public`` for YouTube.
     * ``self`` - The privacy setting is ``self`` for Facebook.
     * ``unlisted`` - The privacy setting is ``unlisted`` for YouTube."""

    provider_destination_id: Optional[str] = UNSET
    """The ID of the destination on the specified service, such as the YouTube channel ID or the Facebook page ID."""

    provider_video_id: OptionalNullable[str] = UNSET
    """The ID of the scheduled video."""

    scheduled_at: Optional[float] = UNSET
    """The time in Unix timestamp format when live streaming is scheduled to start."""

    service_name: ServiceName1OrStr
    """The service to simulcast to.

    Option descriptions:
     * ``custom_rtmp`` - Simulcast to a custom service.
     * ``facebook`` - Simulcast to Facebook Live.
     * ``linkedin`` - Simulcast to LinkedIn Live.
     * ``youtube`` - Simulcast to YouTube Live."""

    stream_key: Optional[str] = UNSET
    """The RTMP stream key."""

    stream_url: Optional[str] = UNSET
    """The RTMP URL for receiving the video stream."""

    type_: Type15OrStr = Field(alias="type")
    """The type of the simulcast destination.

    Option descriptions:
     * ``channel`` - The destination is a YouTube channel.
     * ``custom`` - The destination is custom.
     * ``organization`` - The destination is a LinkedIn organization.
     * ``page`` - The destination is a Facebook page.
     * ``profile`` - The destination is a Facebook or LinkedIn profile."""


class UsersLiveEventsDestinationsRequestDict(TypedDict):
    display_name: str
    is_enabled: NotRequired[bool]
    privacy: NotRequired[Privacy9OrStr]
    provider_destination_id: NotRequired[str]
    provider_video_id: NotRequired[str | None]
    scheduled_at: NotRequired[float]
    service_name: ServiceName1OrStr
    stream_key: NotRequired[str]
    stream_url: NotRequired[str]
    type_: Type15OrStr
