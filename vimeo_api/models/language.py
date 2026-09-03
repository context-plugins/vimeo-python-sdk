from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Language(SdkBaseModel):
    code: str
    """The standard ISO 639-1 code for the language."""

    name: str
    """The name of the language."""


class LanguageDict(TypedDict):
    code: str
    name: str
