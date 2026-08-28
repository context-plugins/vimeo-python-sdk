from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InteractionToolsSettings(SdkBaseModel):
    """The settings for the interaction tools."""

    is_anonymous_questions_disabled: Optional[bool] = UNSET
    """Whether anonymous questions are disabled for the interaction tools settings."""

    is_qna_moderated: Optional[bool] = UNSET
    """Whether the Q&A is moderated for the interaction tools settings."""


class InteractionToolsSettingsDict(TypedDict):
    is_anonymous_questions_disabled: NotRequired[bool]
    is_qna_moderated: NotRequired[bool]
