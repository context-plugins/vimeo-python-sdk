from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buttons8 import Buttons8, Buttons8Dict
from .card2 import Card2, Card2Dict
from .end_screen4 import EndScreen4, EndScreen4Dict
from .logos16 import Logos16, Logos16Dict
from .play_button3 import PlayButton3, PlayButton3Dict
from .sentiment_widget1 import SentimentWidget1, SentimentWidget1Dict
from .title2 import Title2, Title2Dict


class Embed29(SdkBaseModel):
    airplay: Optional[bool] = UNSET
    """Whether AirPlay is enabled in the embeddable player."""

    audio_tracks: Optional[bool] = UNSET
    """Whether multiple audio tracks can appear in the embeddable player."""

    buttons: Optional[Buttons8] = UNSET
    cards: Optional[list[Card2]] = UNSET
    """A collection of cards associated with the selected video."""

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

    context_menu: Optional[bool] = UNSET
    """Whether the right-click context menu appears in the embeddable player."""

    end_screen: Optional[EndScreen4] = UNSET
    logos: Optional[Logos16] = UNSET
    play_button: Optional[PlayButton3] = UNSET
    """An object representing the play button's settings."""

    playbar: Optional[bool] = UNSET
    """Whether to show the playbar on the embeddable player."""

    quality_selector: Optional[bool] = UNSET
    """Whether to show the quality selector in the embeddable player."""

    sentiment_widgets: Optional[list[SentimentWidget1]] = UNSET
    """A collection of sentiment widget configurations for the video."""

    skipping_forward: Optional[bool] = UNSET
    """Whether users can skip forward in the embeddable player."""

    title: Optional[Title2] = UNSET
    transcript: Optional[bool] = UNSET
    """Whether the transcript controls appear in the embeddable player."""

    volume: Optional[bool] = UNSET
    """Whether to show the volume selector on the embeddable player."""


class Embed29Dict(TypedDict):
    airplay: NotRequired[bool]
    audio_tracks: NotRequired[bool]
    buttons: NotRequired[Buttons8 | Buttons8Dict]
    cards: NotRequired[list[Card2 | Card2Dict]]
    cc_track_menu: NotRequired[bool]
    chapters: NotRequired[bool]
    chromecast: NotRequired[bool]
    closed_captions: NotRequired[bool]
    color: NotRequired[str]
    context_menu: NotRequired[bool]
    end_screen: NotRequired[EndScreen4 | EndScreen4Dict]
    logos: NotRequired[Logos16 | Logos16Dict]
    play_button: NotRequired[PlayButton3 | PlayButton3Dict]
    playbar: NotRequired[bool]
    quality_selector: NotRequired[bool]
    sentiment_widgets: NotRequired[list[SentimentWidget1 | SentimentWidget1Dict]]
    skipping_forward: NotRequired[bool]
    title: NotRequired[Title2 | Title2Dict]
    transcript: NotRequired[bool]
    volume: NotRequired[bool]
