from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FolderUri(SdkBaseModel):
    """An object containing data on the value of **folder_uri** and whether it's required for the interaction."""

    required: bool
    """Whether the URI of the folder must be sent to achieve the desired action."""

    value: str
    """The URI of the folder to which the team member should have access."""


class FolderUriDict(TypedDict):
    required: bool
    value: str
