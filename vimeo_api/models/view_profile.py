from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .disabled import Disabled, DisabledDict


class ViewProfile(SdkBaseModel):
    """Information about the user's profile."""

    disabled: Optional[Disabled] = UNSET
    """Information regarding the current authenticated user's inability to access the user's profile."""

    mod_override: Optional[bool] = UNSET
    """Whether the current authenticated user can access the user's profile with a moderator override."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI for the current authenticated user."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the user's profile."""


class ViewProfileDict(TypedDict):
    disabled: NotRequired[DisabledDict]
    mod_override: NotRequired[bool]
    options: NotRequired[list[str]]
    uri: NotRequired[str]
