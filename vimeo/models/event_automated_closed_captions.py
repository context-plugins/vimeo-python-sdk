from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EventAutomatedClosedCaptions(SdkBaseModel):
    auto_cc_can_be_enabled: bool
    """Whether automated closed captions can be enabled."""

    auto_cc_credits_per_minute: float
    """AI credits consumed per minute for auto-captions."""

    auto_cc_enabled: bool
    """Whether the option for automated closed captions is enabled."""

    auto_cc_is_unlimited: bool
    """Whether automated closed captions are unlimited for the user."""

    auto_cc_keywords: str
    """A comma-separated list of keywords for enhancing the speech detection of automated closed captions."""

    auto_cc_language: str | None
    """The language of the automated closed captions."""

    auto_cc_limit: float | None
    """The maximum seconds for automated closed captions (legacy, for users not yet on AI-credit billing)."""

    auto_cc_remaining: float | None
    """The number of seconds remaining for automated closed captions (legacy, for users not yet on AI-credit
    billing)."""

    auto_cc_translation_credits_per_minute: float
    """AI credits consumed per minute per translation language."""

    auto_cc_translation_enabled: bool
    """Whether automated caption translations are enabled."""

    auto_cc_translation_languages: list[str]
    """The list of language codes for caption translations."""

    event_id: float
    """The ID of the event."""


class EventAutomatedClosedCaptionsDict(TypedDict):
    auto_cc_can_be_enabled: bool
    auto_cc_credits_per_minute: float
    auto_cc_enabled: bool
    auto_cc_is_unlimited: bool
    auto_cc_keywords: str
    auto_cc_language: str | None
    auto_cc_limit: float | None
    auto_cc_remaining: float | None
    auto_cc_translation_credits_per_minute: float
    auto_cc_translation_enabled: bool
    auto_cc_translation_languages: list[str]
    event_id: float
