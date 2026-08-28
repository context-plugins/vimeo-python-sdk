from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.encoder_type import EncoderTypeOrStr
from .enums.status14 import Status14OrInt


class Ingest(SdkBaseModel):
    """The ingest of the video."""

    encoder_type: EncoderTypeOrStr
    """The protocol used for this session.

    Option descriptions:
     * ``dash`` - The protocol is DASH.
     * ``rtmp`` - The protocol is RTMP.
     * ``simple_live`` - The protocol is Simplelive.
     * ``srt`` - The protocol is SRT.
     * ``studio_cloud`` - The protocol is StudioCloud.
     * ``unknown`` - The protocol is unknown or not set.
     * ``webrtc`` - The protocol is WebRTC."""

    end_time: float | None
    """The timestamp in UTC format when the live stream ended."""

    height: float | None
    """The height of the live video in pixels."""

    is_rtmp_session: bool
    """Whether the session is using RTMP."""

    is_scheduled_playback: bool | None
    """Whether the stream is scheduled media playback."""

    rtmp_expires_at: str | None
    """The time in ISO 8601 format when the RTMP expires."""

    rtmp_link: str | None
    """The upstream RTMP link. Send your live content to this link to create a live video on the event."""

    rtmps_link: str | None
    """The upstream RTMPS link. Send your live content to this secure link to create a live video on the event."""

    scheduled_start_time: str | None
    """The scheduled start time of the live video in ISO 8601 format."""

    session_id: str | None
    """The session ID."""

    start_time: float | None
    """The timestamp in UTC format when the live video started."""

    status: Status14OrInt | None
    """The ingest status of the live video.

    Option descriptions:
     * ``0`` - There’s a live video, but no RMTP URL or key.
     * ``1`` - There’s an RMTP URL and key, but the machine is provisioning.
     * ``2`` - There’s an RMTP URL and key, and the machine is provisioned, but the stream hasn’t started yet.
     * ``3`` - There’s an RMTP URL and key, and the machine is provisioned, but the stream didn’t start before the
            machine timed out.
     * ``4`` - The stream has started and is currently underway.
     * ``5`` - The stream has ended."""

    stream_ended_reason: float | None
    """The reason why the stream ended. If the stream hasn't ended, this field is empty."""

    stream_key: str | None
    """The stream key used in conjunction with the RTMP and RTMPS links."""

    width: float | None
    """The width of the live video in pixels."""


class IngestDict(TypedDict):
    encoder_type: EncoderTypeOrStr
    end_time: float | None
    height: float | None
    is_rtmp_session: bool
    is_scheduled_playback: bool | None
    rtmp_expires_at: str | None
    rtmp_link: str | None
    rtmps_link: str | None
    scheduled_start_time: str | None
    session_id: str | None
    start_time: float | None
    status: Status14OrInt | None
    stream_ended_reason: float | None
    stream_key: str | None
    width: float | None
