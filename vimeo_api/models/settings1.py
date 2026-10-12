from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .buttons1 import Buttons1, Buttons1Dict
from .colors5 import Colors5, Colors5Dict
from .end_screen1 import EndScreen1, EndScreen1Dict
from .enums.byline import BylineOrStr
from .enums.portrait1 import Portrait1OrStr
from .enums.title1 import Title1OrStr
from .outro import Outro, OutroDict
from .play_button import PlayButton, PlayButtonDict


class Settings1(SdkBaseModel):
    """The contents of the preset group."""

    airplay: bool
    """Whether AirPlay is enabled in the embeddable player."""

    ask_ai: bool
    """Whether Ask AI is enabled in the embeddable player."""

    audio_tracks: bool
    """Whether multiple audio tracks can appear in the embeddable player."""

    buttons: Buttons1
    byline: BylineOrStr
    """How the embeddable player handles the video owner's information.

    Option descriptions:
     * ``hide`` - The owner's information is hidden.
     * ``show`` - The owner's information is shown.
     * ``user`` - The owner's information can be toggled to ``show`` or ``hide`` by the user."""

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

    colors: Colors5
    end_screen: EndScreen1
    """A representation of the end screen settings."""

    outro: Outro
    pip: bool
    """Whether picture-in-picture is enabled and the button appears in the embeddable player."""

    play_button: PlayButton
    """A representation of the play button's settings."""

    playbar: bool
    """Whether the playbar appears in the embeddable player."""

    portrait: Portrait1OrStr
    """How the embeddable player handles the video owner's portrait.

    Option descriptions:
     * ``hide`` - The owner's portrait is hidden.
     * ``show`` - The owner's portrait is shown.
     * ``user`` - The owner's portrait can be toggled to ``show`` or ``hide`` by the user."""

    quality_selector: bool
    """Whether to show the quality selector in the embeddable player."""

    skipping_forward: bool
    """Whether users can skip forward in the embeddable player."""

    speed: bool
    """Whether the speed controls appear in the embeddable player."""

    title: Title1OrStr
    """How the embeddable player handles the video title.

    Option descriptions:
     * ``hide`` - The title is hidden.
     * ``show`` - The title is shown.
     * ``user`` - The title can be toggled to ``show`` or ``hide`` by the user."""

    transcript: bool
    """Whether the transcript controls appear in the embeddable player."""

    volume: bool
    """Whether the volume controls appear in the embeddable player."""


class Settings1Dict(TypedDict):
    airplay: bool
    ask_ai: bool
    audio_tracks: bool
    buttons: Buttons1Dict
    byline: BylineOrStr
    cc_track_menu: bool
    chapters: bool
    chromecast: bool
    closed_captions: bool
    color: str
    colors: Colors5Dict
    end_screen: EndScreen1Dict
    outro: OutroDict
    pip: bool
    play_button: PlayButtonDict
    playbar: bool
    portrait: Portrait1OrStr
    quality_selector: bool
    skipping_forward: bool
    speed: bool
    title: Title1OrStr
    transcript: bool
    volume: bool
