from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Tutorial(SdkBaseModel):
    message: str
    """The success message."""

    next_steps_link: str
    """The link to the next tutorial."""

    token_is_authenticated: bool
    """Whether the current access token is authenticated."""


class TutorialDict(TypedDict):
    message: str
    next_steps_link: str
    token_is_authenticated: bool
