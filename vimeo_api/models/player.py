from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .colors1 import Colors1, Colors1Dict
from .logos1 import Logos1, Logos1Dict
from .play_button1 import PlayButton1, PlayButton1Dict


class Player(SdkBaseModel):
    """The contents of the player group."""

    airplay: Optional[bool] = UNSET
    """Whether AirPlay is enabled in the video page player."""

    audio_tracks: Optional[bool] = UNSET
    """Whether multiple audio tracks can appear in the video page player."""

    autoplay: Optional[bool] = UNSET
    """Whether the video automatically plays for viewers without their own autoplay preference (e.g. logged-out
    visitors)."""

    cc_track_menu: Optional[bool] = UNSET
    """Whether clicking the closed-captions button reveals the caption-language menu in the video page player."""

    chromecast: Optional[bool] = UNSET
    """Whether the Chromecast button appears in the video page player."""

    closed_captions: Optional[bool] = UNSET
    """Whether closed captions are enabled in the video page player."""

    colors: Optional[Colors1] = UNSET
    """A collection of information about the colors in the video page player."""

    context_menu: Optional[bool] = UNSET
    """Whether the right-click menu is shown in the video page player."""

    fullscreen: Optional[bool] = UNSET
    """Whether to display the button for fullscreen mode on the video page."""

    logos: Optional[Logos1] = UNSET
    """A collection of information about the logo in the corner of the onsite player."""

    muted: Optional[bool] = UNSET
    """Whether the video is muted by default for viewers."""

    pip: Optional[bool] = UNSET
    """Whether picture-in-picture is enabled in the video page player."""

    play_button: Optional[PlayButton1] = UNSET
    """A representation of the play button's settings."""

    playbar: Optional[bool] = UNSET
    """Whether to display the playbar on the video page."""

    quality_selector: Optional[bool] = UNSET
    """Whether the quality selector appears in the video page player."""

    skipping_forward: Optional[bool] = UNSET
    """Whether to enable users to skip forward in the embeddable player."""

    speed: Optional[bool] = UNSET
    """Whether to display speed options in the video page player."""

    volume: Optional[bool] = UNSET
    """Whether to display the volume control on the video page."""


class PlayerDict(TypedDict):
    airplay: NotRequired[bool]
    audio_tracks: NotRequired[bool]
    autoplay: NotRequired[bool]
    cc_track_menu: NotRequired[bool]
    chromecast: NotRequired[bool]
    closed_captions: NotRequired[bool]
    colors: NotRequired[Colors1Dict]
    context_menu: NotRequired[bool]
    fullscreen: NotRequired[bool]
    logos: NotRequired[Logos1Dict]
    muted: NotRequired[bool]
    pip: NotRequired[bool]
    play_button: NotRequired[PlayButton1Dict]
    playbar: NotRequired[bool]
    quality_selector: NotRequired[bool]
    skipping_forward: NotRequired[bool]
    speed: NotRequired[bool]
    volume: NotRequired[bool]
