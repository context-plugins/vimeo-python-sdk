from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buttons2 import Buttons2, Buttons2Dict
from .end_screen4 import EndScreen4, EndScreen4Dict
from .logos10 import Logos10, Logos10Dict
from .title2 import Title2, Title2Dict


class Embed18(SdkBaseModel):
    buttons: Optional[Buttons2] = UNSET
    color: Optional[str] = UNSET
    """The main color of the embeddable player."""

    end_screen: Optional[EndScreen4] = UNSET
    logos: Optional[Logos10] = UNSET
    playbar: Optional[bool] = UNSET
    """Whether to show the playbar on the embeddable player."""

    title: Optional[Title2] = UNSET
    volume: Optional[bool] = UNSET
    """Whether to show the volume selector on the embeddable player."""


class Embed18Dict(TypedDict):
    buttons: NotRequired[Buttons2 | Buttons2Dict]
    color: NotRequired[str]
    end_screen: NotRequired[EndScreen4 | EndScreen4Dict]
    logos: NotRequired[Logos10 | Logos10Dict]
    playbar: NotRequired[bool]
    title: NotRequired[Title2 | Title2Dict]
    volume: NotRequired[bool]
