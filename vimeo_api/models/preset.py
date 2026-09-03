from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata23 import Metadata23, Metadata23Dict
from .settings1 import Settings1, Settings1Dict
from .user import User, UserDict


class Preset(SdkBaseModel):
    created_on: str
    """The time in ISO 8601 format when the preset was created."""

    metadata: Metadata23
    """Metadata about the preset."""

    modified_on: str
    """The time in ISO 8601 format when the preset was last modified."""

    name: str
    """The display name of the preset group."""

    settings: Settings1
    """The contents of the preset group."""

    uri: str
    """The canonical relative URI of the preset object."""

    user: User | None
    """The owner of the preset."""


class PresetDict(TypedDict):
    created_on: str
    metadata: Metadata23 | Metadata23Dict
    modified_on: str
    name: str
    settings: Settings1 | Settings1Dict
    uri: str
    user: User | UserDict | None
