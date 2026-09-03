from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AudioTrackQuota(SdkBaseModel):
    """The quota parameters for the audio tracks available for this version."""

    free: float
    """The number of audio tracks availible for this version."""

    has_reached_quota: bool
    """Whether the current version has reached its maximum quota for audio tracks."""

    max: float
    """The maximum number of audio tracks that the user can upload per version based on their subscription tier."""

    used: float
    """The number of audio tracks used for this version."""


class AudioTrackQuotaDict(TypedDict):
    free: float
    has_reached_quota: bool
    max: float
    used: float
