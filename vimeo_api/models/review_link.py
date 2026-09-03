from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ReviewLink(SdkBaseModel):
    allow_comments: bool
    """Whether to allow comments in the review."""

    allow_downloads: bool
    """Whether downloads are permitted in the review."""

    allow_status_change: bool
    """Whether a status change is permitted in the review."""

    created_on: str
    """The time in ISO 8601 format when the review was created."""

    expires_on: str
    """The time in ISO 8601 format when the review expires."""

    hide_end_cards: bool
    """Whether to hide end cards (other videos) after playback."""

    is_dark: bool
    """Whether the review link is in dark mode."""

    is_enabled: bool
    """Whether the review link is enabled."""

    logo_url: str
    """The link to the team logo from the brandkit."""

    modified_on: str
    """The time in ISO 8601 format when the review was last modified."""

    name: str
    """The name of the link."""

    password: str | None
    """The password for the review link."""

    show_all_versions: bool
    """Whether showing all versions is permitted in the review."""

    show_my_logo: bool
    """Whether to display the user's logo in the review."""

    show_resolved_comments: bool
    """Whether to show resolved comments in the review."""

    uri: str
    """The canonical relative URI of the review link."""

    url: str
    """The relative URL of the review link."""


class ReviewLinkDict(TypedDict):
    allow_comments: bool
    allow_downloads: bool
    allow_status_change: bool
    created_on: str
    expires_on: str
    hide_end_cards: bool
    is_dark: bool
    is_enabled: bool
    logo_url: str
    modified_on: str
    name: str
    password: str | None
    show_all_versions: bool
    show_my_logo: bool
    show_resolved_comments: bool
    uri: str
    url: str
