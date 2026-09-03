from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AncestorPath1(SdkBaseModel):
    can_upload: bool
    """Whether the user can upload to this ancestor folder."""

    name: str
    """The name of the folder."""

    uri: str
    """The URI of the ancestor folder."""


class AncestorPath1Dict(TypedDict):
    can_upload: bool
    name: str
    uri: str
