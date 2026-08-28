from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type16 import Type16OrStr


class Graphic(SdkBaseModel):
    id: str
    """The unique identifier of the graphic item."""

    type_: Type16OrStr = Field(alias="type")
    """The type of the graphic item.

    Option descriptions:
     * ``agoraMedia`` - A generic preloaded video or image.
     * ``agoraScreen`` - Shared screen content from an Agora user.
     * ``agoraStream`` - A live video feed from an Agora participant.
     * ``broadcasterLowerthird`` - The name and title for the main host.
     * ``fullscreen`` - A screen-filling informational graphic.
     * ``guestLowerthird`` - The name and title for a stream guest.
     * ``logo`` - A branding or emblem image.
     * ``lowerthird`` - The standard name and title text overlay.
     * ``poll`` - Audience voting content and results.
     * ``qna`` - Question and answer text display.
     * ``slides`` - Presentation slide content."""


class GraphicDict(TypedDict):
    id: str
    type_: Type16OrStr
