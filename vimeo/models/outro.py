from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.type26 import Type26OrStr
from .link1 import Link1, Link1Dict


class Outro(SdkBaseModel):
    clips: OptionalNullable[str] = UNSET
    """A comma-separated list of video URIs. This field appears only when **type** is ``uploaded_clips``."""

    link: OptionalNullable[Link1] = UNSET
    """The outro link settings. These fields appear only when **type** is ``link``."""

    text: OptionalNullable[str] = UNSET
    """The outro text. This appears only when **type** is ``text``."""

    type_: Type26OrStr = Field(alias="type")
    """The preset outro type.

    Option descriptions:
     * ``link`` - The outro includes a link.
     * ``no idea`` - The outro type is ``no idea``. The outro includes uploaded videos.
     * ``text`` - The outro includes text.
     * ``uploaded_clips`` - The outro includes uploaded videos.
     * ``uploaded_videos`` - The outro includes uploaded videos."""

    videos: OptionalNullable[str] = UNSET
    """A comma-separated list of video URIs. This field appears only when **type** is ``no idea``."""


class OutroDict(TypedDict):
    clips: NotRequired[str | None]
    link: NotRequired[Link1 | Link1Dict | None]
    text: NotRequired[str | None]
    type_: Type26OrStr
    videos: NotRequired[str | None]
