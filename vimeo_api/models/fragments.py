from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .metadata18 import Metadata18, Metadata18Dict


class Fragments(SdkBaseModel):
    created_on: str
    """The time in ISO 8601 format when the fragment was created."""

    metadata: Metadata18
    """Metadata about the fragments."""

    modified_on: str
    """The time in ISO 8601 format when the fragment was last updated."""

    timecode: float
    """The time in milliseconds of the fragment's _inpoint_, or the time from the start of the video that marks the
    beginning of the fragment."""

    uri: str
    """The URI of the video fragment."""


class FragmentsDict(TypedDict):
    created_on: str
    metadata: Metadata18Dict
    modified_on: str
    timecode: float
    uri: str
