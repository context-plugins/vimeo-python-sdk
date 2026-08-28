from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.name import NameOrStr
from .enums.owner import OwnerOrStr
from .enums.portrait import PortraitOrStr


class Title(SdkBaseModel):
    """A collection of information about the embeddable player's title bar."""

    name: NameOrStr
    """How the embeddable player handles the video title.

    Option descriptions:
     * ``hide`` - The title is hidden.
     * ``show`` - The title is shown.
     * ``user`` - The title can be toggled to ``show`` or ``hide`` by the user."""

    owner: OwnerOrStr
    """How the embeddable player handles the video owner's information.

    Option descriptions:
     * ``hide`` - The owner's information is hidden.
     * ``show`` - The owner's information is shown.
     * ``user`` - The owner's information can be toggled to ``show`` or ``hide`` by the user."""

    portrait: PortraitOrStr
    """How the embeddable player handles the video owner's portrait.

    Option descriptions:
     * ``hide`` - The owner's portrait is hidden
     * ``show`` - The owner's portrait is shown.
     * ``user`` - The owner's portrait can be toggled to ``show`` or ``hide`` by the user."""


class TitleDict(TypedDict):
    name: NameOrStr
    owner: OwnerOrStr
    portrait: PortraitOrStr
