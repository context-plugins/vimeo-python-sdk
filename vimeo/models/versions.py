from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Versions(SdkBaseModel):
    """Information about the video's versions."""

    create_storyboard_id: Optional[str] = UNSET
    """The storyboard ID of the video version."""

    current_uri: Optional[str] = UNSET
    """The URI of the current version of the video."""

    has_interactive: Optional[bool] = UNSET
    """Whether the video has interactive capability."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    origin_variable_frame_resolution: Optional[bool] = UNSET
    """Whether the video has unified resolution. If the value of this field is ``false``, the video requires
    transcoding."""

    resource_key: Optional[str] = UNSET
    """The resource key string of the current version of the video."""

    sequence_number: float | None
    """The sequence number of the video version."""

    total: Optional[float] = UNSET
    """The total number of versions on this connection."""

    total_including_deleted: Optional[float] = UNSET
    """The total number of versions on this connection, including deleted versions."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class VersionsDict(TypedDict):
    create_storyboard_id: NotRequired[str]
    current_uri: NotRequired[str]
    has_interactive: NotRequired[bool]
    options: NotRequired[list[str]]
    origin_variable_frame_resolution: NotRequired[bool]
    resource_key: NotRequired[str]
    sequence_number: float | None
    total: NotRequired[float]
    total_including_deleted: NotRequired[float]
    uri: NotRequired[str]
