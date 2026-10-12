from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ai_content import AiContent, AiContentDict
from .connections4 import Connections4, Connections4Dict
from .interactions3 import Interactions3, Interactions3Dict


class Metadata4(SdkBaseModel):
    """The video's metadata."""

    ai_content: Optional[AiContent] = UNSET
    """Information about the video's AI content."""

    can_be_replaced: Optional[bool] = UNSET
    """Whether the video can be replaced."""

    connections: Connections4
    """A list of resource URIs related to the video."""

    edit_session_vsid: Optional[float] = UNSET
    """The video's Vimeo Create ID."""

    has_chapter_suggestions: bool
    """Whether the video has chapter suggestions."""

    has_email_capture: Optional[bool] = UNSET
    """Whether the video has the email capture feature."""

    has_interactive_quiz: bool | None
    """The video contains an interactive quiz."""

    has_mandatory_email_capture: Optional[bool] = UNSET
    """Whether the video has mandatory email capture feature."""

    interactions: Interactions3
    """A list of resource URIs related to the video."""

    is_screen_record: bool
    """Whether the video is a screen recording."""

    is_vimeo_create: bool
    """Whether the video is a Vimeo Create video."""

    is_zoom_upload: bool
    """Whether the video is a Zoom upload."""


class Metadata4Dict(TypedDict):
    ai_content: NotRequired[AiContentDict]
    can_be_replaced: NotRequired[bool]
    connections: Connections4Dict
    edit_session_vsid: NotRequired[float]
    has_chapter_suggestions: bool
    has_email_capture: NotRequired[bool]
    has_interactive_quiz: bool | None
    has_mandatory_email_capture: NotRequired[bool]
    interactions: Interactions3Dict
    is_screen_record: bool
    is_vimeo_create: bool
    is_zoom_upload: bool
