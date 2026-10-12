from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .disabled3 import Disabled3, Disabled3Dict


class PublishToSocial(SdkBaseModel):
    """Information about the user's publish-to-social history for the video."""

    disabled: Optional[Disabled3] = UNSET
    """Whether the publish-to-social feature is disabled."""

    options: Optional[list[str]] = UNSET
    """An array of HTTP methods permitted on this URI."""

    publish_blockers: Optional[Any] = UNSET
    """Information about the publish blockers of the video."""

    publish_constraints: Optional[Any] = UNSET
    """Information about the publish constraints of the video."""

    uri: Optional[str] = UNSET
    """The API URI that resolves to the connection data."""


class PublishToSocialDict(TypedDict):
    disabled: NotRequired[Disabled3Dict]
    options: NotRequired[list[str]]
    publish_blockers: NotRequired[Any]
    publish_constraints: NotRequired[Any]
    uri: NotRequired[str]
