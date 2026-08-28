from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class InteractionToolsSetting(SdkBaseModel):
    is_anonymous_questions_disabled: bool
    """Whether anonymous questions are disabled for the interaction tools settings."""

    is_qna_moderated: bool
    """Whether the Q&A is moderated for the interaction tools settings."""


class InteractionToolsSettingDict(TypedDict):
    is_anonymous_questions_disabled: bool
    is_qna_moderated: bool
