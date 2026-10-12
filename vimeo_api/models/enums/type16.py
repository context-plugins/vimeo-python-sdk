from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type16(str, Enum):
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

    AGORA_MEDIA = "agoraMedia"
    AGORA_SCREEN = "agoraScreen"
    AGORA_STREAM = "agoraStream"
    BROADCASTER_LOWERTHIRD = "broadcasterLowerthird"
    FULLSCREEN = "fullscreen"
    GUEST_LOWERTHIRD = "guestLowerthird"
    LOGO = "logo"
    LOWERTHIRD = "lowerthird"
    POLL = "poll"
    QNA = "qna"
    SLIDES = "slides"

    __str__ = str.__str__


Type16OrStr: TypeAlias = Annotated[Type16 | str, open_enum_validator(Type16)]
