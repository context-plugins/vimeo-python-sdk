from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .badges import Badges, BadgesDict
from .buttons import Buttons, ButtonsDict
from .card import Card, CardDict
from .colors import Colors, ColorsDict
from .enums.outro_type import OutroTypeOrStr
from .logos import Logos, LogosDict
from .play_button import PlayButton, PlayButtonDict
from .sentiment_widget import SentimentWidget, SentimentWidgetDict
from .title import Title, TitleDict
from .unions.end_screen3 import EndScreen3, EndScreen3Dict


class EmbedSettings(SdkBaseModel):
    airplay: bool
    """Whether AirPlay is enabled in the embeddable player."""

    ask_ai: bool
    """Whether Ask AI is enabled in the embeddable player."""

    audio_tracks: bool
    """Whether multiple audio tracks can appear in the embeddable player."""

    autopip: bool
    """Whether automatic picture-in-picture is enabled."""

    autoplay: bool
    """Whether the video autoplays in the embeddable player."""

    badges: Badges
    """A collection of the video's badges."""

    buttons: Buttons
    """A collection of information about the buttons that appear on the interface of the embeddable player."""

    cards: list[Card]
    """A collection of cards associated with the selected video."""

    cc_track_menu: bool
    """Whether clicking the closed-captions button reveals the caption-language menu in the embeddable player."""

    chapters: bool
    """Whether chapters are enabled in the embeddable player."""

    chromecast: bool
    """Whether the Chromecast button appears in the embeddable player."""

    closed_captions: bool
    """Whether closed captions are enabled in the embeddable player."""

    color: str
    """The second player color, which controls the player accent color. _This field is identical to
    **colors.color_two**._"""

    colors: Colors
    """A collection of information about player colors."""

    context_menu: bool
    """Whether the right-click context menu appears in the embeddable player."""

    email_capture_form: Any
    """The email capture form settings associated with the video. _This field is deprecated._"""

    end_screen: EndScreen3
    """A collection of information about the embeddable player's end screen. The API returns an empty array instead of
    an object when no end screen is configured for the video."""

    event_schedule: bool
    """Whether the embedded player should display the event schedule."""

    has_cards: bool
    """Whether the video has cards."""

    html: Optional[str] = UNSET
    """The HTML code for embedding the video on a web page."""

    interactive: bool
    """Whether the video is an interactive video."""

    logos: Logos
    """A collection of information about the logo in the corner of the embeddable player."""

    muted: bool
    """Whether the video starts muted in the embeddable player."""

    outro_type: OutroTypeOrStr
    """The type of the video outro.

    Option descriptions:
     * ``beginning`` - The outro is a thumbnail.
     * ``custom`` - The outro is custom.
     * ``email`` - The outro is an email form.
     * ``image`` - The outro is an image.
     * ``link`` - The outro is a link.
     * ``loop`` - The outro is a loop.
     * ``nothing`` - There is no outro.
     * ``share`` - The outro is a share button.
     * ``text`` - The outro is text.
     * ``threevideos`` - The outro is three video suggestions.
     * ``videos`` - The outro is video suggestions."""

    pip: bool
    """Whether picture-in-picture is enabled and the button appears in the embeddable player."""

    play_button: PlayButton
    """A representation of the play button's settings."""

    playbar: bool
    """Whether the playbar appears in the embeddable player."""

    quality_selector: bool
    """Whether the quality selector appears in the embeddable player."""

    sentiment_widgets: list[SentimentWidget]
    """The sentiment widget configuration for the video."""

    show_timezone: bool
    """Whether the embedded player displays the schedule timezone."""

    skipping_forward: bool
    """Whether users can skip forward in the embeddable player."""

    speed: bool
    """Whether the speed controls appear in the embeddable player."""

    title: Title
    """A collection of information about the embeddable player's title bar."""

    transcript: bool
    """Whether the transcript controls appear in the embeddable player."""

    uri: Optional[str] = UNSET
    """The URI of the embed preset."""

    volume: bool
    """Whether the volume controls appear in the embeddable player."""


class EmbedSettingsDict(TypedDict):
    airplay: bool
    ask_ai: bool
    audio_tracks: bool
    autopip: bool
    autoplay: bool
    badges: BadgesDict
    buttons: ButtonsDict
    cards: list[CardDict]
    cc_track_menu: bool
    chapters: bool
    chromecast: bool
    closed_captions: bool
    color: str
    colors: ColorsDict
    context_menu: bool
    email_capture_form: Any
    end_screen: EndScreen3Dict
    event_schedule: bool
    has_cards: bool
    html: NotRequired[str]
    interactive: bool
    logos: LogosDict
    muted: bool
    outro_type: OutroTypeOrStr
    pip: bool
    play_button: PlayButtonDict
    playbar: bool
    quality_selector: bool
    sentiment_widgets: list[SentimentWidgetDict]
    show_timezone: bool
    skipping_forward: bool
    speed: bool
    title: TitleDict
    transcript: bool
    uri: NotRequired[str]
    volume: bool
