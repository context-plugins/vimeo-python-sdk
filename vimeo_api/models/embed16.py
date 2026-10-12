from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buttons2 import Buttons2, Buttons2Dict
from .colors6 import Colors6, Colors6Dict
from .end_screen2 import EndScreen2, EndScreen2Dict
from .logos8 import Logos8, Logos8Dict
from .play_button3 import PlayButton3, PlayButton3Dict
from .title2 import Title2, Title2Dict


class Embed16(SdkBaseModel):
    airplay: Optional[bool] = UNSET
    """Whether AirPlay is enabled in the embeddable player."""

    audio_tracks: Optional[bool] = UNSET
    """Whether multiple audio tracks can appear in the embeddable player."""

    buttons: Optional[Buttons2] = UNSET
    cc_track_menu: Optional[bool] = UNSET
    """Whether clicking the closed-captions button reveals the caption-language menu in the embeddable player."""

    chapters: Optional[bool] = UNSET
    """Whether chapters are enabled in the embeddable player."""

    chromecast: Optional[bool] = UNSET
    """Whether the Chromecast button appears in the embeddable player."""

    closed_captions: Optional[bool] = UNSET
    """Whether closed captions are enabled in the embeddable player."""

    color: Optional[str] = UNSET
    """The main color of the embeddable player."""

    colors: Optional[Colors6] = UNSET
    end_screen: Optional[EndScreen2] = UNSET
    logos: Optional[Logos8] = UNSET
    play_button: Optional[PlayButton3] = UNSET
    """An object representing the play button's settings."""

    playbar: Optional[bool] = UNSET
    """Whether to show the playbar on the embeddable player."""

    quality_selector: Optional[bool] = UNSET
    """Whether to show the quality selector in the embeddable player."""

    skipping_forward: Optional[bool] = UNSET
    """Whether users can skip forward in the embeddable player."""

    title: Optional[Title2] = UNSET
    transcript: Optional[bool] = UNSET
    """Whether the transcript controls appear in the embeddable player."""

    volume: Optional[bool] = UNSET
    """Whether to show the volume selector on the embeddable player."""


class Embed16Dict(TypedDict):
    airplay: NotRequired[bool]
    audio_tracks: NotRequired[bool]
    buttons: NotRequired[Buttons2Dict]
    cc_track_menu: NotRequired[bool]
    chapters: NotRequired[bool]
    chromecast: NotRequired[bool]
    closed_captions: NotRequired[bool]
    color: NotRequired[str]
    colors: NotRequired[Colors6Dict]
    end_screen: NotRequired[EndScreen2Dict]
    logos: NotRequired[Logos8Dict]
    play_button: NotRequired[PlayButton3Dict]
    playbar: NotRequired[bool]
    quality_selector: NotRequired[bool]
    skipping_forward: NotRequired[bool]
    title: NotRequired[Title2Dict]
    transcript: NotRequired[bool]
    volume: NotRequired[bool]
