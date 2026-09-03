from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Language2(SdkBaseModel):
    """The language of the audio track."""

    code: str
    """The standard ISO 639-1 code for the language."""

    name: str
    """The name of the language."""


class Language2Dict(TypedDict):
    code: str
    name: str
