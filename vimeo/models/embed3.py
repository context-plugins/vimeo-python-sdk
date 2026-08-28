from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .colors import Colors, ColorsDict
from .embed_properties import EmbedProperties, EmbedPropertiesDict
from .enums.play_button_position import PlayButtonPositionOrStr
from .logos2 import Logos2, Logos2Dict


class Embed3(SdkBaseModel):
    """The event's embed data."""

    airplay: bool
    """Whether AirPlay is enabled in the embeddable player."""

    autoplay: bool
    """Whether the embedded RLE player should autoplay the RLE content."""

    available_player_logos: list[str]
    """The list of user-uploaded logos for configuration of the embed player."""

    byline: bool
    """Whether the embedded RLE player should display the author's name."""

    chat_embed_source: str | None
    """The chat's iFrame source URL."""

    chromecast: bool
    """Whether the Chromecast button appears in the embeddable player."""

    closed_captions: bool
    """Whether closed captions are enabled in the embeddable player."""

    color: str
    """The second player color, which controls the player accent color. _This field is identical to
    **colors.color_two**._"""

    colors: Colors
    """A collection of information about player colors."""

    embed_chat: str | None
    """The embed code for RLE chat."""

    embed_properties: EmbedProperties | None
    """The height, width, and source URL properties used to generate the fixed HTML embed code."""

    event_schedule: bool
    """Whether the embedded RLE player should display the event schedule."""

    fullscreen_button: bool
    """Whether the embedded RLE player should include the fullscreen controls."""

    hide_live_label: bool
    """Whether the Live label should be visible over the player."""

    hide_viewer_count: bool
    """Whether the embedded RLE player should hide the viewer counter."""

    html: str | None
    """The fixed HTML code to embed the event's playlist on a website."""

    like_button: bool
    """Whether the embedded RLE player should include the button for likes."""

    logos: Logos2
    """A collection of information about the logo in the corner of the embeddable player."""

    loop: bool
    """Whether the embedded RLE player should loop back to the first video once content is exhausted."""

    pip: bool
    """Whether picture-in-picture is enabled and the button appears in the embeddable player."""

    play_button_position: PlayButtonPositionOrStr
    """The position of the player's play button.

    Option descriptions:
     * ``0`` - The play button has the default position.
     * ``1`` - The play button appears at the bottom of the interface.
     * ``2`` - The play button appears in the center of the interface."""

    playbar: bool
    """Whether the embedded RLE player should include the playbar."""

    playlist: bool
    """Whether the playlist component appears in the embeddable player for this RLE."""

    portrait: bool
    """Whether the embedded RLE player should display the author's portrait."""

    responsive_html: str | None
    """The responsive HTML code to embed the event's playlist on a website."""

    schedule: bool
    """Whether the schedule component appears in the embeddable player for this RLE."""

    show_latest_archived_clip: bool
    """Whether the embedded RLE player should display the latest video placeholder."""

    show_timezone: bool
    """Whether the embedded RLE player should display the schedule timezone."""

    title: bool
    """Whether the embedded RLE player should display the video title."""

    transcript: bool
    """Whether transcripts are enabled in the embeddable player."""

    use_color: str
    """Whether the embedded RLE player should use a custom color or the default Vimeo blue."""

    volume: bool
    """Whether the embedded RLE player should include the volume controls."""


class Embed3Dict(TypedDict):
    airplay: bool
    autoplay: bool
    available_player_logos: list[str]
    byline: bool
    chat_embed_source: str | None
    chromecast: bool
    closed_captions: bool
    color: str
    colors: Colors | ColorsDict
    embed_chat: str | None
    embed_properties: EmbedProperties | EmbedPropertiesDict | None
    event_schedule: bool
    fullscreen_button: bool
    hide_live_label: bool
    hide_viewer_count: bool
    html: str | None
    like_button: bool
    logos: Logos2 | Logos2Dict
    loop: bool
    pip: bool
    play_button_position: PlayButtonPositionOrStr
    playbar: bool
    playlist: bool
    portrait: bool
    responsive_html: str | None
    schedule: bool
    show_latest_archived_clip: bool
    show_timezone: bool
    title: bool
    transcript: bool
    use_color: str
    volume: bool
