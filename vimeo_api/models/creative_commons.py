from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.code1 import Code1OrStr


class CreativeCommons(SdkBaseModel):
    code: Code1OrStr
    """The type of Creative Commons license.

    Option descriptions:
     * ``by`` - Attribution.
     * ``by-nc`` - Attribution Non-Commercial.
     * ``by-nc-nd`` - Attribution Non-Commercial No Derivatives.
     * ``by-nc-sa`` - Attribution Non-Commercial Share Alike.
     * ``by-nd`` - Attribution No Derivatives.
     * ``by-sa`` - Attribution Share Alike.
     * ``cc0`` - Public Domain Dedication."""

    name: str
    """The description of the Creative Commons license."""

    uri: str | None
    """The canonical relative URI of the Creative Commons license."""


class CreativeCommonsDict(TypedDict):
    code: Code1OrStr
    name: str
    uri: str | None
