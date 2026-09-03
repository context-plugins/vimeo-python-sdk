from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AncestorPath(SdkBaseModel):
    link: str
    """The link to the folder."""

    name: str
    """The name of the folder."""


class AncestorPathDict(TypedDict):
    link: str
    name: str
